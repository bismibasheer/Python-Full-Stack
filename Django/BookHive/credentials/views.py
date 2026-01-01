from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import auth
from django.contrib import messages
from credentials.models import Profile
from django.db import transaction

# Create your views here.
def register(request):
    if request.method=='POST':
        first_name=request.POST['f_name']
        last_name=request.POST['last_name']
        mail=request.POST['email']
        password=request.POST['create_pass']
        pic=request.FILES.get("profile_pic",None)
        if User.objects.filter(username=mail).exists():
            return HttpResponse("User Already Exists")
        else:
            try:
                with transaction.atomic():
                    user=User.objects.create_user(username=mail,first_name=first_name,last_name=last_name,email=mail,password=password)
                    user.save()
                    Profile.objects.create(user=user,profile_pic=pic)
                    return redirect("sign-in")
            except Exception as e:
                messages.error(request,"Can't create new user {}".format(e))    
    return render(request,"register.html")


def signin(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['passwd']
        user=auth.authenticate(username=email,password=password)
        if user is not None:
            auth.login(request,user)
            if user.profile.role=="manager":
                return redirect('dashboard')
            elif user.profile.role=="user":
                return redirect("listall")
            
        else:
            messages.error(request,"Invalid username or password")
            return redirect("sign-in")
            # return HttpResponse("Invalid username or password")
    return render(request,"Login.html")

def logout(request):
    auth.logout(request)
    return redirect("sign-in")

