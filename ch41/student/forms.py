from django import forms
from student.models import Profile  # Assuming 'Profile' is the model defined in student/models.py

# class Register(forms.Form):
#     name = forms.CharField(max_length=150, required=True, label='name')
#     password = forms.CharField(widget=forms.PasswordInput, required=True, label='Password')
#     email = forms.EmailField(required=True, label='Email')

class Register(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['name', 'password', 'email'] # Using ModelForm to automatically generate fields based on the Profile model
