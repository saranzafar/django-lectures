from django.shortcuts import render, redirect
from blog.forms import CreatePostForm
from blog.models import Post

def home(request):
    print("i called")
    if request.method == "POST":
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreatePostForm()

    blog_posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/home.html', {'form': form, 'blog_posts': blog_posts})
