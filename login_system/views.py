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
    try:
        user_account = get_object_or_404(User, user_name=username, password=password, secret_phrase=secret_phrase)
        context = {
            "user": user_account
        }
        if user_account:
            return render(request, "login_system/account.html", context)
    except User.DoesNotExist as e:
        return e