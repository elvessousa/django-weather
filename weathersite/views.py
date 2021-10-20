from django.shortcuts import render
from urllib.parse import quote
from urllib.request import urlopen
import json

# Create your views here.
def index(request):
    city = ''
    data = ''

    if request.method == 'POST' and request.POST['city'] != '':
        city = request.POST['city']
        url = 'https://api.openweathermap.org/data/2.5/weather'
        key = 'c8ff7df3d166ca5b2551c85066375e86'
        req = urlopen(f'{url}?q={quote(city)}&appid={key}').read()
        raw = json.loads(req)
        data = {
            'name': raw['name'],
            'icon': raw['weather'][0]['icon'],
            'description': raw['weather'][0]['description'],
            'country': raw['sys']['country'],
            'lat': str(raw['coord']['lat']),
            'lon': str(raw['coord']['lon']),
            'temp': f"{raw['main']['temp']}K",
            'celsius': f"{int(raw['main']['temp'] - 273)}ºC",
            'pressure': str(raw['main']['pressure']),
            'humidity': str(raw['main']['humidity'])
        }

    return render(request, 'form.html', {'data': data})
