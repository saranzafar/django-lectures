from django import forms

class Register(forms.Form):
    # Basic Fields 
    first_name = forms.CharField(error_messages={
        'required': 'First name is required',
        'max_length': 'First name cannot exceed 30 characters'
    }, max_length=30)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    def clean_name(self):
        # self.cleaned_data.get('first_name')
        name_value = self.cleaned_data['first_name']
        if len(name_value) < 3:
            raise forms.ValidationError("Name must be at least 3 characters long")
        return name_value

    