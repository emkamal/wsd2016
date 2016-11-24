from django.shortcuts import render, get_object_or_404
from .models import Blog, Post


def index(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/index.html', {'blogs': blogs})

def blog(request, blog_name):
    blog  = get_object_or_404(Blog, slug=blog_name)
    posts = Post.objects.filter(blog=blog)

    return render(request, 'blog/blog.html', {'blog': blog, 'posts': posts})
