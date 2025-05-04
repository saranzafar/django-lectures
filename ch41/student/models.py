from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=150, verbose_name='Name', blank=False)
    password = models.CharField(max_length=150, verbose_name='Password')
    email = models.EmailField(verbose_name='Email')