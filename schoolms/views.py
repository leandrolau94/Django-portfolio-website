from django.shortcuts import render
from .models import Professor, Group, Student, Subject

# Create your views here.
def index(request):
    return render(request, "schoolms/index.html")

def get_start(request):
    return render(request, "schoolms/get_start.html")

def create_account(request):
    username = request.POST['username_prof']
    email = request.POST['email_prof']
    password = request.POST['password_prof']
    if Professor.objects.filter(user_name=username).exists():
        error_message = "Username has already been taken. Please enter a different one."
        context = {
            "error_message": error_message
        }
        return render(request, "schoolms/get_start.html", context)
    else:
        new_account = Professor(user_name=username, email=email, password=password)
        new_account.save()
        success_created = "Account succesfully created, please log in to continue."
        context = {
            "success_created": success_created,
        }
        return render(request, "schoolms/login_page.html", context)

def login_page(request):
    return render(request, "schoolms/login_page.html")

def log_in(request):
    user = request.POST['user_login']
    password = request.POST['password_login']
    if Professor.objects.filter(user_name=user, password=password).exists():
        professor = Professor.objects.get(user_name=user, password=password)
        context = {
            "professor": professor
        }
        return render(request, "schoolms/account.html", context)
    else:
        error_login_msg = "Incorrect username or password. Please try again."
        context = {
            "error_login_msg": error_login_msg
        }
        return render(request, "schoolms/login_page.html", context)