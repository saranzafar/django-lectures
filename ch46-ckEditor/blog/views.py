from django.shortcuts import render, redirect, get_object_or_404
from blog.forms import CreatePostForm
from blog.models import Post


def home(request):
    # Handle form submission
    if request.method == "POST":
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreatePostForm()

    return render(request, 'blog/home.html', {'form': form})


def blog_list(request):
    blogs = Post.objects.all().order_by('-created_at')
    return render(request, "blog/blog_list.html", {"blogs": blogs})


def blog_detail(request, slug):
    blog = get_object_or_404(Post, slug=slug)
    return render(request, "blog/blog_detail.html", {"blog": blog})
