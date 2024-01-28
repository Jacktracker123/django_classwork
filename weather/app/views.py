from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    context={}
    api_key='360e4bc3865e745ec844bd7ec054ca11'
    city='Mumbai'
    if request.method=='POST':
        city=request.POST.get('city')
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response=requests.get(url)
    data=response.json()
    context['city']=city
    context['weather']=data['weather'][0]['description']
    context['temperature']=data['main']['temp']
    context['max_temp']=data['main']['temp_max']
    context['min_temp']=data['main']['temp_min']
    context['feels_like']=data['main']['feels_like']
    return render(request,'index.html',context)

 
