from django.contrib import admin
from student.models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'dob', 'gender', 'locality', 'city', 'pin', 'state', 'mobile', 'email', 'job_city', 'profile_image', 'my_file']
