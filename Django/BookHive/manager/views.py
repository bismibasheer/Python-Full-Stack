from django.shortcuts import render

# Create your views here.
def managerDashboard(request):
    return render(request,"manager-dashboard.html")

def Addauthor(request):
    return render(request,"Addauthor.html")

def Allauthor(request):
    return render(request,"Allauthor.html")
