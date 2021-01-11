from django.shortcuts import render, redirect
from Posts.models import Post, Comment
from Groups.models import Group
from Posts.forms import postform
from Groups.forms import GroupForm
from .models import Match
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required(login_url='/login/')
def Home(request):
    mypostform = postform(request.POST or None, request.FILES or None)
    newgroupform = GroupForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if newgroupform.is_valid():
            newGroup = newgroupform.save(commit=False)
            newGroup.owner = request.user.profile
            newGroup.save()
            newGroup.members.add(request.user.profile)
            print(newGroup.name, newGroup.slug)
            return redirect('Groups:group', newGroup.slug)

    user = request.user
    friends = user.profile.get_friends()
    groups = user.profile.get_groups()
    matches = Match.objects.all()
    # --------------------get all related posts------------------------
    allposts = Post.objects.filter(author=user.profile, group=None)

    for friend in friends:
        friendposts = Post.objects.filter(author=friend.profile, group=None)
        allposts = allposts | friendposts
    for group in groups:
        groupposts = Post.objects.filter(group=group)
        allposts = allposts | groupposts
    # ------------------------------------------------------------------
    context = {
        'user': user,
        'friends': friends,
        'allposts': allposts,
        'postform': mypostform,
        'groups': groups,
        'newgroupform': newgroupform,
        'matches': matches,
    }
    return render(request, 'Homepage/home.html', context)


def savedposts(request):
    user = request.user
    newgroupform = GroupForm(request.POST or None, request.FILES or None)
    groups = user.profile.get_groups()
    savedposts = user.profile.get_saved_posts()
    context = {
        'groups': groups,
        'newgroupform': newgroupform,
        'savedposts': savedposts,
    }
    return render(request, 'Homepage/savedposts.html', context)
