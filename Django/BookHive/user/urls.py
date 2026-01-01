from django.urls import path
from user import views


urlpatterns = [

    path('allauthor/',views.Allauthor,name="listall"),
    path("author-details/<slug:link>",views.authorDetail,name="author-detail"),
    path('list-books',views.AllBooksView.as_view(),name="list_books"),
    path('book-detail/<slug:book_link>',views.BookDetail.as_view(),name="book_detail"),
    path('books/<slug:slug>/like/',views.bookLike,name="book_like"),
]