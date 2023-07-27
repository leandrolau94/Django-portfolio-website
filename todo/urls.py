from django.urls import path
from . import views

app_name = "todo"
urlpatterns = [
    path('', views.index, name='index'),
    path('create_category/', views.create_category, name='create_category'),
]