from django.db import models

# Create your models here.
class Profile (models.Model):
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=255)
    city = models.CharField(max_length=70)
    roll = models.IntegerField()
    
    # def __str__(self):
        # return str(self.roll)
        # return self.name 
    
class Result (models.Model):
    student_class = models.CharField(max_length=70)
    marks = models.IntegerField()
    
    # def __str__(self):
    #     return self.student_class 
    
