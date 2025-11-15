from django.urls import path
from manager import views


urlpatterns = [
    path("",views.managerDashboard,name="dashboard"),
    path('addauthor/',views.Addauthor,name="addall"),
    path('allauthor/',views.Allauthor,name="listall"),
]
