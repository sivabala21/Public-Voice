from django.urls import path
from . import views

# app_name='pb'

urlpatterns = [
    path('',views.home,name="home"),
    path("create/", views.create, name="create"),
    path("user/",views.user,name="user"),
    path('logout/',views.userLogout,name="logout"),

]
