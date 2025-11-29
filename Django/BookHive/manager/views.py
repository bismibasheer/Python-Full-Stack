from django.shortcuts import render,redirect
from manager.models import Author
from django.utils.text import slugify
from django.contrib import auth
# Create your views here.
def managerDashboard(request):
    user="Bismi"
    return render(request,"manager-dashboard.html",{"name":user})

def Addauthor(request):
    if request.method=="POST":
        name=request.POST['author_name']
        dob=request.POST['dob']
        profile=request.POST['about']
        place=request.POST['place']
        profile_pic=request.FILES['picture']
        link=slugify(name)
        writer=Author(name=name,place=place,about=profile,dob=dob,image=profile_pic,slug=link)
        writer.save()
        return redirect("listall")
    return render(request,"Addauthor.html")

def Allauthor(request):
    malayalam_authors = Author.objects.all()
    print(malayalam_authors)
    return render(request,"Allauthor.html",{"authors":malayalam_authors})

def authorDetail(request,link):
    writer=Author.objects.get(slug=link)
    print(writer)
    return render(request,"author-detail.html",{"author":writer})

def editauthor(request,link):
    author=Author.objects.get(slug=link)
    if request.method=="POST":
        name=request.POST['author_name']
        dob=request.POST['dob']
        profile=request.POST['about']
        place=request.POST['place']
        profile_pic=request.FILES.get('picture')
        author.name=name
        author.dob=dob
        author.place=place
        author.about=profile
        if profile_pic:
            author.image=profile_pic
        author.save()
        return redirect("author-detail",author.slug)
    return render(request,"edit-author.html",{"writer":author})

def deleteauthor(request,link):
    writer=Author.objects.get(slug=link)
    writer.delete()
    return redirect("listall")

def logout(request):
    auth.logout(request)
    return redirect("sign-in")