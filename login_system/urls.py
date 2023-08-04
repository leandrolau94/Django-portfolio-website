from django.urls import path
from . import views

app_name = "login_system"
urlpatterns = [
    path('', views.index, name='index'),
    path('log_in/', views.log_in, name='log_in'),
]