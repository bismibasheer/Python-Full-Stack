from django.shortcuts import render,redirect,get_object_or_404
from manager.models import Author,Book,BookLike
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView,DetailView



# Create your views here.
@login_required(login_url="sign-in")
def Allauthor(request):
    malayalam_authors = Author.objects.all()
    print(malayalam_authors)
    return render(request,"Allauthor.html",{"authors":malayalam_authors})

def authorDetail(request,link):
    writer=Author.objects.get(slug=link)
    # print(writer)
    books=writer.books.all()
    return render(request,"author-detail.html",{"author":writer,"books":books})


class AllBooksView(ListView):
    template_name="all-books.html"
    queryset=Book.objects.all()
    context_object_name="books"

class BookDetail(DetailView):
    template_name="book-details.html"
    model=Book
    context_object_name="book"
    slug_field="slug"
    slug_url_kwarg="book_link"

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["is_liked"]=self.object.likes.filter(user=self.request.user).exists()
        return context
    

def bookLike(request,slug):
    book=get_object_or_404(Book,slug=slug)
    like,created=BookLike.objects.get_or_create(book=book,user=request.user)
    if not created:
        like.delete()
        messages.info(request,"you  unliked this book")
    else:
        messages.success(request,"you liked this book")
    return redirect(book.get_absolute_url())     