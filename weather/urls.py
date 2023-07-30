from django.urls import path
from . import views

app_name = "weather"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('get_weather_info/', views.get_weather_info, name='get_weather_info'),
]