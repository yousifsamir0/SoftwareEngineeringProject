from django.shortcuts import render, redirect
from .models import Group, Grouprequest
from Posts.forms import postform
from .forms import GroupForm
from Profile.models import Profile
from django.http import JsonResponse


# Create your views here.


def group(request, slug):

    group = Group.objects.get(slug=slug)
    editform = GroupForm(
        request.POST or None, request.FILES or None, instance=group)
    mypostform = postform(request.POST or None, request.FILES or None)
    newgroupform = GroupForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if editform.is_valid():
            editform.save()
            return redirect('Groups:group', group.slug)
    groupPosts = group.get_posts()
    user = request.user
    members = group.members.all()
    is_requested = len(Grouprequest.objects.filter(
        group=group).filter(sender=user.profile))
    grouprequests = group.reqs.all()
    groups = user.profile.get_groups()
    context = {
        'group': group,
        'user': user,
        'posts': groupPosts,
        'members': members,
        'is_requested': is_requested,
        'editform': editform,
        'postform': mypostform,
        'reqs': grouprequests,
        'groups': groups,
        'newgroupform': newgroupform,
    }
    return render(request, 'Groups/group.html', context)


def removemember(request, groupslug):
    if request.is_ajax():
        memberslug = request.GET.get('memberslug')
        member = Profile.objects.get(slug=memberslug)
        group = Group.objects.get(slug=groupslug)
        group.members.remove(member)
        return JsonResponse({}, status=200)


def acceptreq(request, slug):
    if request.is_ajax():
        reqslug = request.GET.get('reqslug')
        print(reqslug)
        requester = Profile.objects.get(slug=reqslug)
        group = Group.objects.get(slug=slug)
        GRequest = Grouprequest.objects.get(sender=requester, group=group)
        GRequest.delete()
        group.members.add(requester)
        return JsonResponse({}, status=200)


def refusereq(request, slug):
    if request.is_ajax():
        reqslug = request.GET.get('reqslug')
        requester = Profile.objects.get(slug=reqslug)
        group = Group.objects.get(slug=slug)
        GRequest = Grouprequest.objects.get(sender=requester, group=group)
        GRequest.delete()
        return JsonResponse({}, status=200)


def join(request, slug):
    sender = request.user.profile
    group = Group.objects.get(slug=slug)
    request, created = Grouprequest.objects.get_or_create(
        sender=sender, group=group)

    return redirect('Groups:group', slug)


def cancelrequest(request, slug):
    sender = request.user.profile
    group = Group.objects.get(slug=slug)
    request = Grouprequest.objects.filter(
        sender=sender, group=group).first()
    request.delete()
    return redirect('Groups:group', slug)


def leavegroup(request, slug):
    member = request.user.profile
    group = Group.objects.get(slug=slug)
    group.members.remove(member)
    return redirect('Groups:group', slug)
