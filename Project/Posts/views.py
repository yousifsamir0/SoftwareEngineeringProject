from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Comment, Post
from .forms import postform
from Groups.models import Group
import datetime


# Create your views here.


def postcomment(request):
    profile = request.user.profile
    if request.is_ajax():
        commentbody = request.GET.get('commentbody')
        postpk = int(request.GET.get('postpk'))
        post = Post.objects.get(pk=postpk)
        Comment.objects.create(author=profile, body=commentbody, post=post)
        created = datetime.datetime.now().strftime("%b, %d, %Y, %I:%M %p")

        return JsonResponse({"avatar": profile.avatar.url, "author": profile.get_name(), "created": created}, status=200)


def savepost(request):
    profile = request.user.profile
    if request.is_ajax():
        issaved = False
        postpk = int(request.GET.get('postpk'))
        post = Post.objects.get(pk=postpk)
        savedby = post.saved_by.all()
        if (profile in savedby):
            issaved = False
            post.saved_by.remove(profile)
        else:
            issaved = True
            post.saved_by.add(profile)

    return JsonResponse({'issaved': issaved, }, status=200)


def likepost(request):
    profile = request.user.profile
    islike = False
    if request.is_ajax():
        postpk = int(request.GET.get('postpk'))
        post = Post.objects.get(pk=postpk)
        likedby = post.liked_by.all()
        if (profile in likedby):
            islike = False
            post.liked_by.remove(profile)
        else:
            islike = True
            post.liked_by.add(profile)

        return JsonResponse({"islike": islike}, status=200)


def hpost(request):
    if request.method == 'POST':
        mypostform = postform(request.POST or None, request.FILES or None)
        if mypostform.is_valid():
            post = mypostform.save(commit=False)
            post.author = request.user.profile
            post.save()
            return redirect('Homepage:homepage')


def ppost(request):
    if request.method == 'POST':
        mypostform = postform(request.POST or None, request.FILES or None)
        if mypostform.is_valid():
            post = mypostform.save(commit=False)
            post.author = request.user.profile
            post.save()
            return redirect('Profile:myprofile')


def grouppost(request, slug):
    mypostform = postform(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        group = Group.objects.get(slug=slug)
        if mypostform.is_valid():
            post = mypostform.save(commit=False)
            post.author = request.user.profile
            post.group = group
            post.save()
            return redirect('Groups:group', group.slug)
