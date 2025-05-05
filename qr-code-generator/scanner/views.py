from django.shortcuts import render
from django.contrib import messages
from django.views import View
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from pathlib import Path
import json, hashlib, uuid, logging
from io import BytesIO
from PIL import Image
from pyzbar.pyzbar import decode

from .models import QRCode, QRCodeUsageLog
from .forms import GenerateQRForm, ScanQRForm

from qrcode import QRCode as QRCodeGenerator
from qrcode.constants import ERROR_CORRECT_H
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer, SquareModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask

logger = logging.getLogger(__name__)

class QRCodeManager:
    @staticmethod
    def generate_styled_qr(data, style):
        # Initialize QR generator with high error correction
        qr = QRCodeGenerator(version=1, error_correction=ERROR_CORRECT_H, box_size=10, border=4)
        qr.add_data(data)
        qr.make(fit=True)

        # Apply selected style (modern or corporate)
        if style == 'modern':
            return qr.make_image(
                image_factory=StyledPilImage,
                module_drawer=RoundedModuleDrawer(),
                color_mask=SolidFillColorMask(back_color=(255, 255, 255), front_color=(0, 48, 135))
            )
        elif style == 'corporate':
            return qr.make_image(
                image_factory=StyledPilImage,
                module_drawer=SquareModuleDrawer(),
                color_mask=SolidFillColorMask(back_color=(248, 250, 252), front_color=(15, 23, 42))
            )

        # Default fallback style
        return qr.make_image(fill_color="black", back_color="white")

    @staticmethod
    def generate_filename(data, mobile):
        # Generate unique filename using hash of data and timestamp
        content = f"{data}_{mobile}_{timezone.now().isoformat()}"
        h = hashlib.md5(content.encode()).hexdigest()[:12]
        return f"qr_{h}.png"

class GenerateQRView(View):
    def get(self, request):
        return render(request, 'scanner/generate.html', {'form': GenerateQRForm()})

    def post(self, request):
        form = GenerateQRForm(request.POST)
        if not form.is_valid():
            return render(request, 'scanner/generate.html', {'form': form})

        # Extract form data
        data = form.cleaned_data['qr_text']
        mobile = form.cleaned_data['mobile']
        style = form.cleaned_data['style'].lower()

        # Compose JSON payload to encode
        qr_id = str(uuid.uuid4())[:8]
        metadata = {
            'id': qr_id,
            'data': data,
            'mobile': mobile,
            'created_at': timezone.now().isoformat(),
            'type': 'payment_token'
        }
        qr_content = json.dumps(metadata)

        # Generate styled QR image
        img = QRCodeManager.generate_styled_qr(qr_content, style)

        # Save QR image to memory
        bio = BytesIO()
        img.save(bio)
        bio.seek(0)
        # Save to media/qr_codes/ using FileSystemStorage
        fs = FileSystemStorage(location=str(settings.MEDIA_ROOT / 'qr_codes'), base_url=settings.MEDIA_URL + 'qr_codes/')
        filename = QRCodeManager.generate_filename(data, mobile)
        saved = fs.save(filename, bio)
        url = fs.url(saved)

        # Save QRCode instance
        qr = QRCode.objects.create(
            qr_id=qr_id,
            data=data,
            mobile_number=mobile,
            image=f"qr_codes/{filename}",
            metadata=metadata
        )

        # Log generation
        QRCodeUsageLog.objects.create(
            qr_code=qr,
            action='generated',
            ip_address=request.META.get('REMOTE_ADDR')
        )

        # Success feedback
        messages.success(request, 'QR code generated!')

        # Render page with image preview
        return render(request, 'scanner/generate.html', {
            'form': GenerateQRForm(),
            'qr_image_url': url,
            'qr_id': qr_id,
            'qr_data': data,
            'mobile_number': mobile
        })


class ScanQRView(View):
    def get(self, request):
        return render(request, 'scanner/scan.html', {'form': ScanQRForm()})

    def post(self, request):
        form = ScanQRForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'scanner/scan.html', {'form': form})

        mobile = form.cleaned_data['mobile']
        uploaded = form.cleaned_data['qr_image']

        # Save uploaded file temporarily
        fs = FileSystemStorage()
        tmp_name = fs.save(f"tmp_{uuid.uuid4().hex[:8]}_{uploaded.name}", uploaded)
        tmp_path = Path(fs.location) / tmp_name

        qr = None  # Ensure qr is always defined
        try:
            img = Image.open(tmp_path)
            decoded = decode(img)

            if not decoded:
                raise ValueError("No QR found")

            content = decoded[0].data.decode().strip()

            # Handle JSON-based (our style) or fallback QR content
            try:
                qr_data = json.loads(content)
                qr_id = qr_data['id']
                stored_mobile = qr_data['mobile']
                payment_data = qr_data['data']
            except (json.JSONDecodeError, KeyError):
                parts = [p.strip() for p in content.split('|', 1)]
                payment_data, stored_mobile = parts if len(parts) == 2 else (None, None)
                qr_id = None

            if stored_mobile != mobile:
                raise ValueError("Mobile mismatch")

            # Match QR code by ID or fallback fields
            qs = QRCode.objects.filter(qr_id=qr_id, is_active=True) if qr_id else \
                 QRCode.objects.filter(data=payment_data, mobile_number=mobile, is_active=True)

            qr = qs.first()
            if not qr:
                raise ValueError("Not found or used")

            # Update scan log
            qr.increment_scan_count()
            qr.deactivate()
            QRCodeUsageLog.objects.create(qr_code=qr, action='scanned', ip_address=request.META.get('REMOTE_ADDR'))

            result = {
                'success': True,
                'mobile': mobile,
                'data': payment_data,
                'qr_id': qr.qr_id,
                'amount': payment_data if payment_data is not None and payment_data.replace('.', '').isdigit() else None
            }

            messages.success(request, 'Scanned successfully!')
            return render(request, 'scanner/scan.html', {'form': ScanQRForm(), 'result': result})

        except Exception as e:
            logger.warning(f"QR scan failed: {str(e)}")

            QRCodeUsageLog.objects.create(
                qr_code=qr if 'qr' in locals() else None,
                action='failed_scan',
                additional_data={'error': str(e)}
            )

            messages.error(request, str(e))
            return render(request, 'scanner/scan.html', {'form': form})

        finally:
            if tmp_path.exists():
                tmp_path.unlink()  # Always clean up the temp file
