from django.contrib import admin
from student.models import Profile, Result

# Register your models here.
# admin.site.register(Profile)
# admin.site.register(Result)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','name','roll','city')
    
admin.site.register(Profile, ProfileAdmin) # register the sub class


# class ResultAdmin(admin.ModelAdmin):
#     list_display = ('id','student_class','marks')
    
# admin.site.register(Result, ResultAdmin)

@admin.register(Result) #Decorator
class ResultAdmin(admin.ModelAdmin):
    list_display = ('id','student_class','marks')