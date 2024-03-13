from django.shortcuts import render
from .models import Blog

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blog_list.html', {'blogs': blogs})

def blog_detail(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, 'blog/blog_detail.html', {'blog': blog})
    

