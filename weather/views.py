import  requests
from django.shortcuts import render

def index(request):
    appid = 'b952d80df29c93133f97626538066e22'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=' + appid

    city = 'London'
    res = requests.get(url.format(city))
    print(res.text)
    return render(request, 'weather/index.html')
