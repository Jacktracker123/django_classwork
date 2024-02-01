from django.shortcuts import render
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
# Create your views here.

def add_user(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        uname=request.POST['uname']
        password=request.POST['password']
        user=User.objects.create_user(first_name=fname,last_name=lname,username=uname,password=password)
        user.save()
        return HttpResponse('Data saved')
    else:
        return render(request,'form.html')
        

def login_user(request):
    if request.method=="POST":
        uname=request.POST['uname']
        password=request.POST['password']
        login=auth.authenticate(username=uname,password=password)
        if login:
            auth.login(request,login)
            return render(request,'home.html')
        else:
            return HttpResponse('User not exist')
    else:
        return render(request,'login.html')