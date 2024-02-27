from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")


def create(request):
    return render(request,"create.html")


def user(request):
    return render(request,"user.html")


