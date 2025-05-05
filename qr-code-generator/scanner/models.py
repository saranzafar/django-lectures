from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone
import uuid
import os
from django.dispatch import receiver

def qr_image_upload_path(instance, filename):
    return os.path.join('qr_codes', filename)

def generate_qr_id():
    # return a unique string each call — importable by Django’s migration writer
    return str(uuid.uuid4())

class QRCode(models.Model):
    qr_id = models.CharField(
        max_length=36,
        unique=True,
        default=generate_qr_id,
        help_text="Unique identifier for the QR code"
    )

    data = models.TextField(help_text="The main data/content encoded in the QR code")
    mobile_number = models.CharField(
        max_length=11,
        validators=[RegexValidator(regex=r'^03\d{9}$', message='Must be 11 digits starting with 03')],
        help_text="11-digit mobile number starting with 03"
    )
    image = models.ImageField(
        upload_to=qr_image_upload_path,
        max_length=255,
        help_text="QR code image file"
    )
    metadata = models.JSONField(default=dict, blank=True, help_text="Additional metadata")
    is_active = models.BooleanField(default=True, help_text="Whether still valid")
    created_at = models.DateTimeField(auto_now_add=True, help_text="When generated")
    scanned_at = models.DateTimeField(null=True, blank=True, help_text="When scanned")
    scan_count = models.PositiveIntegerField(default=0, help_text="Times scanned")
    qr_type = models.CharField(
        max_length=50,
        default='payment',
        choices=[('payment','Payment'),('verification','Verification'),('access','Access Control'),('info','Information')]
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    expires_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['qr_id']), models.Index(fields=['mobile_number','is_active']),
            models.Index(fields=['created_at']), models.Index(fields=['qr_type','is_active'])
        ]

    def __str__(self):
        return f"QR-{self.qr_id}"

    def is_expired(self):
        if not self.expires_at:
            return False
        return timezone.now() > self.expires_at

    def increment_scan_count(self):
        self.scan_count = models.F('scan_count') + 1
        self.save(update_fields=['scan_count'])

    def deactivate(self):
        self.is_active = False
        self.scanned_at = timezone.now()
        self.save(update_fields=['is_active','scanned_at'])

@receiver(models.signals.post_delete, sender=QRCode)
def delete_qr_image(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)


class QRCodeUsageLog(models.Model):
    qr_code = models.ForeignKey(QRCode, on_delete=models.CASCADE, related_name='usage_logs')
    action = models.CharField(max_length=20, choices=[
        ('generated','Generated'),('scanned','Scanned'),
        ('failed_scan','Failed Scan'),('expired','Expired'),
    ])
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    additional_data = models.JSONField(default=dict, blank=True)

    class Meta:
        ordering = ['-timestamp']
        indexes = [models.Index(fields=['qr_code','action']), models.Index(fields=['timestamp'])]

    def __str__(self):
        return f"{self.qr_code.qr_id} - {self.action}"
