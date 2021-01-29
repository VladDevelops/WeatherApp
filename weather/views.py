import  requests
from django.shortcuts import render

def index(request):
    appid = 'b952d80df29c93133f97626538066e22'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    city = 'London'
    res = requests.get(url.format(city)).json()

    city_info = {
         'city': city,
         'temp': res["main"]["temp"] ,
         'icon': res["weather"][0]["icon"]
    }

    context = {'info': city_info}
    return render(request, 'weather/index.html', context)
