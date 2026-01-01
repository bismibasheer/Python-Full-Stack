from django.urls import path
from manager import views


urlpatterns = [
    path("",views.managerDashboard,name="dashboard"),
    path('addauthor/',views.Addauthor,name="addall"),

    path("edit-author/<slug:link>",views.editauthor,name="editauthor"),
    path("deleteauthor/<slug:link>",views.deleteauthor,name="deleteauthor"),
    
    # Books
    path('addbook/',views.addbook,name="addbook"),

    path('update-book/<slug:book_slug>',views.UpdateBook.as_view(),name="edit_book"),
    path('delete-book/<slug:slug>',views.DeleteBook.as_view(),name="delete-book"),
    
   
]
