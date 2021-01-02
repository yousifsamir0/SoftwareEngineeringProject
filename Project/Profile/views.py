from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Profile, FriendRequest
from django.contrib.auth.decorators import login_required
from .forms import editProfileForm
from Posts.forms import postform
from Posts.models import Post


# Create your views here.
@login_required(login_url='/login/')
def myprofile(request):
    slug = Profile.objects.get(user=request.user).slug
    return redirect('Profile:profile', slug)


@login_required(login_url='/login/')
def profile(request, slug='myprofile'):
    mypostform = postform(request.POST or None, request.FILES or None)
    editform = editProfileForm(request.POST or None,
                               request.FILES or None, instance=request.user.profile)
    if request.method == 'POST':
        if editform.is_valid():
            editform.save()
            return redirect('Profile:myprofile')
        if mypostform.is_valid():
            post=mypostform.save(commit=False)
            post.author=request.user.profile
            post.save()
            return redirect('Profile:myprofile')

    profile = Profile.objects.get(slug=slug)
    user = request.user

    is_requested = len(FriendRequest.objects.filter(
        reciever=profile).filter(sender=user.profile))
    friendrequests = FriendRequest.objects.filter(reciever=user.profile)
    context = {
        'profile': profile,
        'user': user,
        'is_requested': is_requested,
        'friendreqs': friendrequests,
        'editform': editform,
        'postform': mypostform,
    }

    return render(request, 'profile/profile.html', context)


def addfriend(request, slug):
    sender = request.user.profile
    receiver = Profile.objects.get(slug=slug)
    request, created = FriendRequest.objects.get_or_create(
        sender=sender, reciever=receiver)

    return redirect('Profile:profile', slug)


def cancelrequest(request, slug):
    sender = request.user.profile
    receiver = Profile.objects.get(slug=slug)
    request = FriendRequest.objects.filter(
        sender=sender, reciever=receiver).first()
    request.delete()
    return redirect('Profile:profile', slug)


def acceptrequest(request, slug):
    sender = Profile.objects.get(slug=slug)
    receiver = request.user.profile
    request = FriendRequest.objects.filter(
        sender=sender, reciever=receiver).first()
    sender.friends.add(receiver.user)
    receiver.friends.add(sender.user)
    request.delete()
    return redirect('Profile:myprofile')


def refuserequest(request, slug):
    sender = Profile.objects.get(slug=slug)
    receiver = request.user.profile
    request = FriendRequest.objects.filter(
        sender=sender, reciever=receiver).first()
    request.delete()

    return redirect('Profile:myprofile')
