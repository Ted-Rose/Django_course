from django.urls import path
# From current directory import views
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    # When /blog/int is accessed, views.detail will be called
    path('<int:blog_id>', views.detail, name='detail'),
]