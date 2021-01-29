import  requests
from django.shortcuts import render
from .models import City

def index(request):
    appid = 'b952d80df29c93133f97626538066e22'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid


    cities = City.objects.all()
    all_cities = []

    for city in  cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"] ,
            'icon': res["weather"][0]["icon"]
      }

      all_cities.append(city_info)


    context = {'all_info': all_cities}
    return render(request, 'weather/index.html', context)
