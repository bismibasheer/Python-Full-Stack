from django.shortcuts import render,redirect,get_object_or_404
from manager.models import Author,Book,BookLike
from django.utils.text import slugify
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BookForm
from django.views.generic import ListView,UpdateView,DetailView,DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy,reverse


# Create your views here.

@login_required(login_url="sign-in")
def managerDashboard(request):
    user="Bismi"
    return render(request,"manager-dashboard.html",{"name":user})

@login_required(login_url="sign-in")
def Addauthor(request):
    if request.method=="POST":
        name=request.POST['author_name']
        dob=request.POST['dob']
        profile=request.POST['about']
        place=request.POST['place']
        profile_pic=request.FILES.get('picture',None)
        # link=slugify(name)
        writer=Author(name=name,place=place,about=profile,dob=dob,image=profile_pic)
        writer.save()
        messages.success(request," New Author Added")
        return redirect("listall")
    return render(request,"Addauthor.html")




@login_required(login_url="sign-in")
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
        messages.success(request,"Updated Author Details")
        return redirect("author-detail",author.slug)
    return render(request,"edit-author.html",{"writer":author})


@login_required(login_url="sign-in")
def deleteauthor(request,link):
    writer=Author.objects.get(slug=link)
    writer.delete()
    messages.success(request,"Author Deleted")
    return redirect("listall")

@login_required(login_url="sign-in")
def addbook(request):

    if request.method == "POST":
        my_form = BookForm(request.POST, request.FILES)
        if my_form.is_valid():
            my_form.save()
            messages.success(request, "New Book Added")
            return redirect("addbook")
    else:
        my_form = BookForm()   # <-- important for GET request

    return render(request, "add-book.html", {"form": my_form})






class UpdateBook(SuccessMessageMixin,UpdateView):
    template_name="update-book.html"
    form_class=BookForm
    model=Book
    slug_field="slug"
    slug_url_kwarg="book_slug"
    success_url="/manager/list-books"
    success_message="Book Details Updated"

    def get_success_url(self):
        return reverse('book_detail',kwargs={"book_link":self.object.slug})


class DeleteBook(DeleteView):
    model=Book
    slug_field="slug" 
    success_url=reverse_lazy("list_books")


       


    
    
   
