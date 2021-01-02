from django.shortcuts import render
from django.http import JsonResponse
from .models import Comment, Post
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
