from django import forms
from student.models import Profile

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

JOB_CITY_CHOISES = [
    ('Karachi', 'Karachi'),
    ('Lahore', 'Lahore'),
    ('Islamabad', 'Islamabad'),
    ('Peshawar', 'Peshawar'),
    ('Quetta', 'Quetta'),
    ('Multan', 'Multan'),
    ('Faisalabad', 'Faisalabad'),
    ('Hyderabad', 'Hyderabad'),
    ('Gujranwala', 'Gujranwala'),
    ('Sialkot', 'Sialkot'),
    ('Rawalpindi', 'Rawalpindi'),
    ('Gujrat', 'Gujrat'),
    ('Bahawalpur', 'Bahawalpur'),
    ('Sargodha', 'Sargodha'),
    ('Sheikhupura', 'Sheikhupura'),
]

class ProfileForm(forms.ModelForm):
    gender = forms.ChoiceField(
        choices = GENDER_CHOICES,
        widget=forms.RadioSelect,
        initial='M',
    )
    job_city = forms.MultipleChoiceField(
        choices=JOB_CITY_CHOISES,
        widget=forms.CheckboxSelectMultiple(),
        label='Preferred Job Cities',
        help_text='Select one or more cities where you prefer to work.',
    )
    class Meta:
        model = Profile
        fields = [
            'name',
            'dob',
            'gender',
            'locality',
            'city',
            'job_city',
            'pin',
            'state',
            'mobile',
            'email',
            'profile_image',
            'my_file',
        ]
        labels = {
            'name': 'Full Name',
            'dob': 'Date of Birth',
            'pin': 'PIN Code',
            'mobile': 'Mobile Number',
        }
        help_texts = {
            'profile_image': 'Upload a profile image (optional)',
            'my_file': 'Upload a file (optional)',
        }
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'dob' : forms.DateInput(attrs={'class':'form-control', 'id':'datepicker', 'type':'date'}),
            'gender' : forms.TextInput(attrs={'class':'form-control'}),
            'locality' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your area name'}),
            'city' : forms.TextInput(attrs={'class':'form-control'}),
            'pin' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'6-digits PIN code'}),
            'state' : forms.Select(attrs={'class':'form-control'}),
            'mobile' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your mobile number'}),
            'email' : forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter your email address'}),
            'my_file' : forms.FileInput(attrs={'class':'form-control'}),
        }