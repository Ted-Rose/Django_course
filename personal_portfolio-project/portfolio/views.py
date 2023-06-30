from django.shortcuts import render
from .models import Project

def home(request):
    # Grab all db objects
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects})
