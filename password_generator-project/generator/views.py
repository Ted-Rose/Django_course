from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):


    # List individual characters into list
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!@£$%^&*()'))

    if request.GET.get('numbers'):
        characters.extend(list('123456789'))
    # Get value of key length in url
    # You can hard code the value to 100 example and it would
    # generate password with 100 characters - it can be handled by
    # adding if statements
    # 12 sets the default value
    length = int(request.GET.get('length', 12))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)


    return render(request, 'generator/password.html', {'password':thepassword})

def about(request):
    return render(request, 'generator/about.html')