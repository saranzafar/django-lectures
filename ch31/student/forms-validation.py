from django import forms

class Register(forms.Form):
    # Basic Fields 
    first_name = forms.CharField(
        label='Full Name',
        max_length=100,
        label_suffix=':',
        # initial='Enter Your Full Name',
        help_text='Enter Your Legal Name Here',
        
        # Validate that input has at least 3 characters 
        # validators=[MinLengthValidator(3)]
    )
    last_name = forms.CharField(initial='Doe', disabled=True)
    email = forms.EmailField()
    pin_code = forms.IntegerField()
    
    # Additional Fields 
    age = forms.FloatField()
    date_of_birth = forms.DateField()
    appoinment_time = forms.DateTimeField()
    meeting_time = forms.TimeField(
        widget=forms.TimeInput(
            attrs={'type':'time', 'placeholder': 'HH-MM-SS'}
        )
    )
    meeting_date = forms.TimeField(
        widget=forms.DateInput(
            attrs={'type':'date', 'placeholder': 'YY:MM:DD'}
        )
    )
    is_subscribed = forms.BooleanField()
    agree_terms = forms.NullBooleanField()
    
    #Choise Fields
    gender = forms.ChoiceField(choices= [
        ('M','Male'),
        ('F','Female'),
        ('O','Other')
    ])
    intrest = forms.MultipleChoiceField(choices= [
        ('tech','Technology'),
        ('art','Art'),
        ('sports','Sports')
    ])
    
    # File and URL Fields 
    profile_image = forms.ImageField()
    resume = forms.FileField()
    website = forms.URLField()

    # Other Specialized Fields 
    phone_number = forms.RegexField(regex=r'^\+?\d{9,15}$')
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'Placeholder':'Enter Password'}
    ))
    slug = forms.SlugField()
    ip_address = forms.GenericIPAddressField()
    rating = forms.DecimalField()
    blog = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'Enter multiple lines of text...'}
        )
    )

    