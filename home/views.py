from django.shortcuts import render
from .models import post
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def home(request):
    posts=post.objects.all()
    return render(request,"home.html",{'posts':posts})

@login_required(login_url='/user')
def create(request):
    if request.method=="POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        if content is not None and content.strip() != '':  # Check if content is not empty
            createPost=post(title=title,content=content,user=request.user)
            createPost.save()
            return HttpResponseRedirect(reverse(home))
        
    return render(request,"create.html")


def user(request):
    if request.method=="POST":
        auth=authenticate(request,username=request.POST["username"],password=request.POST["password"])
        print(auth)
        if auth is not None :
            login(request,auth)
            return HttpResponseRedirect(reverse(home))
        else:
            return render(request,"user.html",{'message':"Invaild Creditionals"})

    return render(request,"user.html")


def userLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse(home))

