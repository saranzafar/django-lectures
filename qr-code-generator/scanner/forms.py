from django import forms
from django.core.validators import FileExtensionValidator
from .models import QRCode

class GenerateQRForm(forms.Form):
    mobile = forms.CharField(
        max_length=11, min_length=11,
        widget=forms.TextInput(attrs={'placeholder':'03xxxxxxxxx'}),
        help_text="11-digit mobile number starting with 03"
    )
    qr_text = forms.CharField(help_text="Payment amount or text")
    style = forms.ChoiceField(choices=[('modern','Modern'),('corporate','Corporate')], initial='modern')

    def clean_mobile(self):
        mobile = ''.join(filter(str.isdigit, self.cleaned_data['mobile']))
        if not mobile.startswith('03'):
            raise forms.ValidationError("Must start with 03")
        return mobile

class ScanQRForm(forms.Form):
    mobile = forms.CharField(
        max_length=11, min_length=11,
        widget=forms.TextInput(attrs={'placeholder':'03xxxxxxxxx'})
    )
    qr_image = forms.ImageField(
        validators=[FileExtensionValidator(['png','jpg','jpeg'])],
        help_text="PNG/JPG up to 5MB"
    )

    def clean_mobile(self):
        mobile = ''.join(filter(str.isdigit, self.cleaned_data['mobile']))
        if not mobile.startswith('03'):
            raise forms.ValidationError("Must start with 03")
        return mobile

    def clean_qr_image(self):
        img = self.cleaned_data['qr_image']
        if img.size > 5*1024*1024:
            raise forms.ValidationError("Image too large (max 5MB)")
        return img
