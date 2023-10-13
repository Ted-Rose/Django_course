from django.shortcuts import render
from .models import Project

def home(request):
    # Grab all db objects
    projects = Project.objects.all()
    # 'projects' is the name of the variable that can be named differently
    return render(request, 'portfolio/home.html', {'projects':projects})
