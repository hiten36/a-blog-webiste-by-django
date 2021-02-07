from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='bloghome'),
    path('postcomm',views.postcomm,name='postcomm'),
    path('<str:slug>',views.blogpost,name='blogpost'),
]