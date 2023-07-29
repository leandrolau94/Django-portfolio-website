from typing import Any
from django.db.models.query import QuerySet
import requests
from django.shortcuts import render
from django.views import generic

weather_url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m,relativehumidity_2m,dewpoint_2m,apparent_temperature,precipitation_probability,precipitation,rain,showers,snowfall,snow_depth"

# Create your views here.
class IndexView(generic.ListView):
    context_object_name = "weather"
    template_name = 'weather/index.html'

    def get_queryset(self):
        r = requests.get(weather_url)
        return r.content