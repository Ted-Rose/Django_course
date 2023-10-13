from django.shortcuts import render
from .models import Blog

def all_blogs(request):
    # Grab latest 5 db objects ordered by date descending
    blogs = Blog.objects.order_by('-date')[:5]
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})