from django.urls import path
from . import views

app_name = 'schoolms'
urlpatterns = [
    path('', views.index, name='index'),
]