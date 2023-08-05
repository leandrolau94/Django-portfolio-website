from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
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