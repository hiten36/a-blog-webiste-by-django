from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import post,blogcomment
from django.contrib import messages

# Create your views here.
def index(request):
    posts=post.objects.all()
    params={'posts':posts}
    return render(request,'blog/index.html',params)

def blogpost(request,slug):
    posts=post.objects.filter(post_slug=slug)
    posts1=post.objects.filter(post_slug=slug).first()
    posts1.post_views=posts1.post_views + 1
    posts1.save()
    comms=blogcomment.objects.filter(comm_post=posts[0])
    comms12=blogcomment.objects.filter(comm_post=posts[0],comm_parent=None)
    replies=blogcomment.objects.filter(comm_post=posts[0]).exclude(comm_parent=None)
    params={'posts':posts,'comms':comms,'user':request.user,'replies':replies,'slug':slug,'comms12':comms12}
    return render(request,'blog/blogpost.html',params)

def postcomm(request):
    if request.method=='POST':
        comm=request.POST.get('comm')
        post_sno=request.POST.get('post_sno')
        post1=post.objects.get(post_sno=post_sno)
        slug1=request.POST.get('slug')
        for comment in blogcomment.objects.all():
            if comment.comm_slug == slug1:
                if comm == comment.comm_comment:
                    messages.error(request,"the comment you are posting is already been posted by another person.")
                    return redirect(f'/blog/{post1.post_slug}')
        comm1=request.POST.get('comm1')
        user=request.user
        post_slug=post1.post_slug
        parent_sno=request.POST.get('parent_sno')
        if parent_sno == '':
            comms1=blogcomment(comm_comment=comm,comm_user=user,comm_post=post1,comm_slug=post_slug)
            messages.success(request,'Comment has been posted!')
        else:
            parent=blogcomment.objects.get(comm_sno=parent_sno)
            comms1=blogcomment(comm_comment=comm1,comm_user=user,comm_post=post1,comm_parent=parent,comm_slug=post_slug)
            messages.success(request,'Reply has been posted!')
        comms1.save()
        
        return redirect(f'/blog/{post1.post_slug}')
    return redirect('/')