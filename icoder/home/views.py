from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import contact
from django.contrib import messages
from blog.models import post
from itertools import chain
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    posts=post.objects.all()[0:3]
    params={'posts':posts}
    return render(request,'home/index.html',params)

def about(request):
    return render(request,'home/about.html')

def contact1(request):
    if request.method=='POST':
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        if len(name)<3 and len(email)<8 and len(phone)<10:
            messages.error(request,'Please fill the form correctly')
        cons=contact(con_name=name,con_email=email,con_phone=phone,con_desc=desc)
        cons.save()
        messages.success(request,'Your query has been submitted successfully!')
    return render(request,'home/contact.html')

def search(request):
    query=request.GET.get('query','')
    if len(query)>58:
        posts=[]
    else:
        posts1=post.objects.filter(post_title__icontains=query)
        posts2=post.objects.filter(post_desc__icontains=query)
        posts3=post.objects.filter(post_author__icontains=query)
        posts1=posts1.union(posts2,posts3)
    params={'posts':posts1,'query':query}
    return render(request,'home/search.html',params)

def handlesignin(request):
    if request.method=='POST':
        user=request.POST.get('user')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        pass1=request.POST.get('pass')
        cpass1=request.POST.get('cpass')
        if len(user)<3:
            messages.error(request,'Username must be between 3-16 in length')
            return redirect('/')
        if len(user)>16:
            messages.error(request,'Username must be between 3-16 in length')
            return redirect('/')
        if not user.isalnum():
            messages.error(request,'Username must only contains numbers and alphabets')
            return redirect('/')
        if pass1!=cpass1:
            messages.error(request,'Please check and renter password')
            return redirect('/')
        users=User.objects.create_user(user,email,pass1)
        users.first_name=fname
        users.last_name=lname
        users.save()
        messages.success(request,"Your account has been created successfully.You can now Login.")
        return redirect('/')
    else:
        return HttpResponse('Error 404 - Not Found')
def handlelogin(request):
    if request.method=='POST':
        user1=request.POST.get('user1')
        pass2=request.POST.get('pass1')
        users=authenticate(username=user1,password=pass2)
        if users is not None:
            login(request,users)
            messages.success(request,'You have been logged in successfully')
            return redirect('/')
        else:
            messages.error(request,'Invalid Credentails,Please retry')
            return redirect('/')
    else:
        return HttpResponse('Error 404 - Not Found')

def handlelogout(request):
    logout(request)
    messages.success(request,"logged out successfully")
    return redirect('/')
