from django.contrib import admin
from student.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'email', 'password')
    search_fields = ('first_name', 'email')
# Register your models here.
