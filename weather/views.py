from typing import Any
from django.db.models.query import QuerySet
import requests
from django.shortcuts import render
from django.views import generic

openweather_api_key = "786c40df863560a493ab62d34fe142b8"
weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={72.3}&lon={45}&appid={openweather_api_key}"

def generate_weather_url(lon, lat):
    return f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={openweather_api_key}"

# Create your views here.
class IndexView(generic.ListView):
    context_object_name = "weather"
    template_name = 'weather/index.html'

    def get_queryset(self):
        r = requests.get(weather_url)
        # print(r.json())
        data = r.json()
        return data

def get_weather_info(request):
    lat = request.POST['lat']
    lon = request.POST['lon']
    url = generate_weather_url(lon, lat)
    r = requests.get(url)
    data = r.json()
    context = {
        "weather": data,
    }
    return render(request, "weather/index.html", context)