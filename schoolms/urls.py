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
    path('add_new_student/<int:group_id>/', views.add_new_student, name='add_new_student'),
    path('student_dashboard/<int:group_dash_id>/', views.student_dashboard, name='student_dashboard'),
    path('delete_group/<int:group_del_id>/', views.delete_group, name='delete_group'),
    path('edit_group_information/<int:edit_group_id>/', views.edit_group_information, name='edit_group_information'),
]