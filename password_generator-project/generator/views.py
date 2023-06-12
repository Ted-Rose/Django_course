from django.shortcuts import render
from django.http import HttpResponse
import string
import  secrets

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):

    length = int(request.GET.get("length"))
    special_character = request.GET.get("special_caharacter")
    numbers = request.GET.get("numbers")
    alphabet = request.GET.get("aplphabet")
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    full_pack = ""
    thepassword = ""

    if special_character == "on":
        full_pack += ''.join(special_chars)
    if numbers == "on":
        full_pack += ''.join(digits)
    if alphabet == "on":
        full_pack += ''.join(letters)
    
    if len(full_pack) == 0:
        thepassword = "Too_ease_too_hack_try_again"
        return render(request, "generator/password.html", {"password": thepassword})

    for i in range(length):
        thepassword += ''.join(secrets.choice(full_pack))

    return render(request, "generator/password.html", {"password": thepassword})

def about(request):

    return render(request, "generator/about.html")