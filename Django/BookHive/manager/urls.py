from django.urls import path
from manager import views


urlpatterns = [
    path("",views.managerDashboard,name="dashboard"),
    path('addauthor/',views.Addauthor,name="addall"),
    path('allauthor/',views.Allauthor,name="listall"),
    path("author-details/<slug:link>",views.authorDetail,name="author-detail"),
    path("edit-author/<slug:link>",views.editauthor,name="editauthor"),
    path("deleteauthor/<slug:link>",views.deleteauthor,name="deleteauthor"),
    path("logout",views.logout,name="logout"),
]
