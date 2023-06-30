from django.contrib import admin
from .models import Project

# Add model Project within /admin
# Things in bold ar obligatory and in regular are optional
admin.site.register(Project)