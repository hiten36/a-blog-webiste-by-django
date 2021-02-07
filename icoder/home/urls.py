from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact1,name='contact'),
    path('search',views.search,name='search'),
    path('signin',views.handlesignin,name='signin'),
    path('login',views.handlelogin,name='login'),
    path('logout',views.handlelogout,name='logout'),
]