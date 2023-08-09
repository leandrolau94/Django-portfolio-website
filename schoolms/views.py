from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
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
        professor_groups = professor.group_set.all()
        context = {
            "professor": professor,
            "professor_groups": professor_groups
        }
        return render(request, "schoolms/account.html", context)
    else:
        error_login_msg = "Incorrect username or password. Please try again."
        context = {
            "error_login_msg": error_login_msg
        }
        return render(request, "schoolms/login_page.html", context)

def create_new_group(request, professor_id):
    professor = Professor.objects.get(id=professor_id)
    group_name = request.POST['group_name']
    academic_level = request.POST['academic_level']
    professor.group_set.create(group_name=group_name, academic_level=academic_level)
    professor_groups = professor.group_set.all()
    context = {
        "professor": professor,
        "professor_groups": professor_groups
    }
    return render(request, "schoolms/account.html", context)

def add_new_student(request, group_id):
    student_name = request.POST['student_name']
    student_age = int(request.POST['student_age'])
    student_genre = request.POST['student_genre']
    group = Group.objects.get(id=group_id)
    group.student_set.create(name=student_name, age=student_age, genre=student_genre)
    professor = Professor.objects.get(id=group.professor_id)
    professor_groups = professor.group_set.all()
    context = {
        "professor": professor,
        "professor_groups": professor_groups
    }
    return render(request, "schoolms/account.html", context)

def student_dashboard(request, group_dash_id):
    group = Group.objects.get(id=group_dash_id)
    students = group.student_set.all()
    professor = Professor.objects.get(id=group.professor_id)
    context = {
        "group": group,
        "students": students,
        "professor": professor
    }
    return render(request, "schoolms/student_dashboard.html", context)

def delete_group(request, group_del_id):
    group = Group.objects.get(id=group_del_id)
    professor = Professor.objects.get(id=group.professor_id)
    group.delete()
    professor_groups = professor.group_set.all()
    context = {
        "professor": professor,
        "professor_groups": professor_groups
    }
    return render(request, "schoolms/account.html", context)

def edit_group_information(request, edit_group_id):
    edit_group_name = request.POST['edit_group_name']
    edit_academic_level = request.POST['edit_academic_level']
    edit_group = Group.objects.get(id=edit_group_id)
    edit_group.group_name = edit_group_name
    edit_group.academic_level = edit_academic_level
    edit_group.save()
    professor = Professor.objects.get(id=edit_group.professor_id)
    professor_groups = professor.group_set.all()
    context = {
        "professor": professor,
        "professor_groups": professor_groups
    }
    return render(request, "schoolms/account.html", context)