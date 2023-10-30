from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method=='POST':
        userName=request.POST['username']
        firstName = request.POST['first_name']
        secondName = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['conformPassword']
        if password1==password2:
            if User.objects.filter(username=userName).exists():
                messages.info(request,"username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=userName,first_name=firstName,last_name=secondName,email=email,password=password1)
                user.save();
                print("user created")
                messages.info(request,"user created")
                return redirect('login')
        else:
            messages.info(request,"password not matching")
            return redirect('register')
    return render(request,"register.html")
