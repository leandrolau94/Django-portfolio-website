from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import Category, Task

# Create your views here.
def index(request):
    categories = Category.objects.all()
    categories_label = [
        "cars", "clothes", "food", "friends", "games", "health", "homework",
        "insurance", "money", "sport", "study", "travel", "vacation", "work"
    ]
    context = {
        "categories": categories,
        "categories_label": categories_label
    }
    return render(request, 'todo/index.html', context)

def create_category(request):
    new_category_name = request.POST['category']
    new_category = Category(category_name=new_category_name, pub_date=timezone.now())
    new_category.save()
    return HttpResponseRedirect(reverse('todo:index'))