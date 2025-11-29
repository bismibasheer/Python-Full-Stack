from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import auth

# Create your views here.
def register(request):
    if request.method=='POST':
        first_name=request.POST['f_name']
        last_name=request.POST['last_name']
        mail=request.POST['email']
        password=request.POST['create_pass']
        if User.objects.filter(username=mail).exists():
            return HttpResponse("User Already Exists")
        else:
            user=User.objects.create_user(username=mail,first_name=first_name,last_name=last_name,email=mail,password=password)
            user.save()
            return redirect("sign-in")
    return render(request,"register.html")


def signin(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['passwd']
        user=auth.authenticate(username=email,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('dashboard')
        else:
            return HttpResponse("Invalid username or password")
    return render(request,"Login.html")

