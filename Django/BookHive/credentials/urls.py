from django.urls import path
from credentials import views


urlpatterns = [
    path("register",views.register,name="sign-up"),
    path("",views.signin,name="sign-in"),
    path("logout",views.logout,name="logout"),

    ]