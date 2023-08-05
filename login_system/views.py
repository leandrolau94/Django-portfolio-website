from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import User

# Create your views here.
def index(request):
    return render(request, "login_system/index.html")

def log_in(request):
    username = request.POST['username']
    password = request.POST['password']
    secret_phrase = request.POST['secret']
    if User.objects.filter(user_name=username, password=password, secret_phrase=secret_phrase).exists():
        user_account = User.objects.get(user_name=username, password=password, secret_phrase=secret_phrase)
        context = {
            "user": user_account
        }
        return render(request, "login_system/account.html", context)
    else:
        context = {
            "error_message": "User Name, Password or Secret Phrase incorrect."
        }
        return render(request, "login_system/index.html", context)

def create_account(request):
    return render(request, "login_system/create_account.html")

def create_new_account(request):
    new_username = request.POST['created_username']
    new_password = request.POST['created_password']
    new_secret_phrase = request.POST['created_secret']
    if User.objects.filter(user_name=new_username).exists():
        error_message = "User Name it's already been taken. Please tap a different one."
        context = {
            "error_message": error_message
        }
        return render(request, "login_system/create_account.html", context)
    else:
        new_account = User(user_name=new_username, password=new_password, secret_phrase=new_secret_phrase)
        new_account.save()
        return HttpResponseRedirect(reverse("login_system:index"))