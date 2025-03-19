from django.db import models

# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=200)
    city=models.CharField(max_length=100)
    roll=models.IntegerField()
    state=models.CharField(max_length=100)
    comment=models.CharField(max_length=100, default='No comment')
    

    
    
