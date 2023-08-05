from django.urls import path
from . import views

app_name = "login_system"
urlpatterns = [
    path('', views.index, name='index'),
    path('log_in/', views.log_in, name='log_in'),
    path('create_account/', views.create_account, name='create_account'),
    path('create_new_account/', views.create_new_account, name='create_new_account'),
]