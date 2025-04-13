from django.db import models

# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)  # Ensure email is unique
    password = models.CharField(max_length=128)  # Use a suitable length for hashed passwords

    
