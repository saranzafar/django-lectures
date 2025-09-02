from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Post(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.TextField(max_length=300)
    content = CKEditor5Field(config_name='extends')
    featured_image = models.ImageField(upload_to='blog_images/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
