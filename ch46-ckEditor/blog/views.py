from django.shortcuts import render
from blog.forms import CreatePostForm
from blog.models import Post

# Create your views here.
def home(request):
    form = CreatePostForm()
    blog_posts = Post.objects.all()
    return render(request, 'blog/home.html', {'form':form, 'blog_posts':blog_posts})