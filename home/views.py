from django.shortcuts import render, get_object_or_404
from .models import post
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def home(request):
    if request.method=="POST":
        username=str(request.user)
        if username != "AnonymousUser":
            print(request.user)
            post_id=request.POST.get("post_id")
            selected_post = get_object_or_404(post, pk=post_id)
            selected_post.upvote()
        else:
            posts=post.objects.order_by('-upvotes')
            return render(request,"home.html",{'posts':posts,'isloggedin':True})
    posts=post.objects.order_by('-upvotes')
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

        if auth is not None :
            login(request,auth)
            return HttpResponseRedirect(reverse(home))
        else:
            return render(request,"user.html",{'message':"Invaild Creditionals"})

    return render(request,"user.html")

def userCreate(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        newuser=User.objects.create_user(username=username,password=password)
        newuser.save
        return HttpResponseRedirect(reverse('user'))
    return render(request,'signup.html')


def userLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse(home))

