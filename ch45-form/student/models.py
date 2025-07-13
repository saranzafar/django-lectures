from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

def validate_pin_length(value):
    if len(str(value)) != 6:
        raise ValidationError("PIN code must be exactly 6 digits long.")

STATE_CHOISE = (
    ('sindh', 'Sindh'),
    ('punjab', 'Punjab'),
    ('kpk', 'Khyber Pakhtunkhwa'),
    ('balochistan', 'Balochistan'),
    ('gilgit', 'Gilgit-Baltistan'),
    ('islamabad', 'Islamabad'),
    ('azad_kashmir', 'Azad Kashmir'),
)

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=1)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin = models.PositiveIntegerField(validators=[validate_pin_length],help_text="Enter a 6-digit PIN code")
    state = models.CharField(max_length=20, choices=STATE_CHOISE, default='sindh')
    # mobile = models.CharField(max_length=15, validators=[RegexValidator(regex=r'^\d{10}$')], help_text="Enter a valid mobile number")
    mobile = models.CharField(max_length=15, help_text="Enter a valid mobile number")
    email = models.EmailField()
    job_city = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True)
    my_file = models.FileField(upload_to='docs/', blank=True)
    