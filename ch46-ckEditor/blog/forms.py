from django import forms
from blog.models import Post
from django_ckeditor_5.widgets import CKEditor5Widget

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'short_description', 'content', 'featured_image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'short_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'content': CKEditor5Widget(attrs={'class': 'django_ckeditor_5'}, config_name='extends'),
            'featured_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
