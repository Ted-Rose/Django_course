from django.shortcuts import render
from .models import Project


def home(request):
    my_projects = Project.objects.all()
    return render(request, 'my_projects/home.html', {"my_projects":my_projects})