from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils import timezone
from .models import Category, Task

# Create your views here.
class IndexView(generic.ListView):
    template_name = "todo/index.html"
    context_object_name = "categories_and_labels"

    def get_queryset(self):
        categories = Category.objects.all()
        categories_label = [
            "cars", "clothes", "food", "friends", "games", "health", "homework",
            "insurance", "money", "sport", "study", "travel", "vacation", "work"
        ]
        context = {
            "categories": categories,
            "categories_label": categories_label
        }
        return context

class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = "todo/category_detail.html"

def create_category(request):
    new_category_name = request.POST['category']
    new_category = Category(category_name=new_category_name, pub_date=timezone.now())
    new_category.save()
    return HttpResponseRedirect(reverse('todo:index'))

def create_task(request):
    category = Category.objects.get(pk=request.POST['category_id'])
    category.task_set.create(
        task_description=request.POST['task_description'],
        created_at=timezone.now()
    )
    return HttpResponseRedirect(reverse('todo:detail', args=(request.POST['category_id'],)))

def task_delete(request):
    category = Category.objects.get(pk=request.POST['category_id_del'])
    task = category.task_set.filter(pk=request.POST['task_id_del'])
    task.delete()
    return HttpResponseRedirect(reverse('todo:detail', args=(request.POST['category_id_del'],)))