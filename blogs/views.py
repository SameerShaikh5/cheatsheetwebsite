from django.shortcuts import render, HttpResponse
from .models import Blog

# Create your views here.
def blog(request):
    blogs = Blog.objects.all().order_by('-date')
    return render(request, 'blogs.html', {'blogs':blogs})


def blogpost(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, 'post.html', {'blog':blog})

