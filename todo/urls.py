from django.urls import path
from . import views

app_name = "todo"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>', views.CategoryDetailView.as_view(), name='detail'),
    path('create_category/', views.create_category, name='create_category'),
    path('create_task/', views.create_task, name='create_task'),
    path('task_delete/', views.task_delete, name='task_delete'),
]