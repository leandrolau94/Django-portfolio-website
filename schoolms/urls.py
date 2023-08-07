from django.urls import path
from . import views

app_name = 'schoolms'
urlpatterns = [
    path('', views.index, name='index'),
    path('get_start/', views.get_start, name='get_start'),
    path('create_account/', views.create_account, name='create_account'),
    path('login_page/', views.login_page, name='login_page'),
    path('log_in/', views.log_in, name='log_in'),
    path('create_new_group/<int:professor_id>/', views.create_new_group, name='create_new_group'),
]