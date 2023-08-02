from typing import Any
from django.db.models.query import QuerySet
import requests
from django.shortcuts import render
from django.views import generic

openweather_api_key = "786c40df863560a493ab62d34fe142b8"
weather_url = f"https://api.openweathermap.org/data/2.5/weather?appid={openweather_api_key}&lat={72.3}&lon={45}"

# Create your views here.
class IndexView(generic.ListView):
    context_object_name = "weather"
    template_name = 'weather/index.html'

    def get_queryset(self):
        try:
            r = requests.get(weather_url)
            # print(r.json())
            data = r.json()
            return data
        except Exception as e:
            return e

def get_weather_info(request):
    lat = request.POST['lat']
    lon = request.POST['lon']
    url = f"https://api.openweathermap.org/data/2.5/weather?appid={openweather_api_key}"
    payload = {'lat': lat, 'lon': lon}
    try:
        r = requests.get(url, params=payload)
        data = r.json()
        context = {
            "weather": data,
        }
        # print(r.json())
        return render(request, "weather/index.html", context)
    except Exception as e:
        return e