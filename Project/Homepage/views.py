from django.shortcuts import render, redirect
from Posts.models import Post, Comment
from Groups.models import Group
from Posts.forms import postform
from Groups.forms import GroupForm
from django.contrib.auth.decorators import login_required
from requests import get
import json
import datetime


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
    # --------------------get all related posts------------------------
    allposts = Post.objects.filter(author=user.profile, group=None)

    for friend in friends:
        friendposts = Post.objects.filter(author=friend.profile, group=None)
        allposts = allposts | friendposts
    for group in groups:
        groupposts = Post.objects.filter(group=group)
        allposts = allposts | groupposts

    # ------------------------------------------------------------------
    # ------------------------ Football-api -----------------------------

    today = datetime.datetime.now().strftime("%Y-%m-%d")
    tomorrow = (datetime.datetime.now() +
                datetime.timedelta(days=1)).strftime("%Y-%m-%d")

    headers = {"apikey": "44cbf3a0-5475-11eb-8878-c57f02f827e2"}
    params = (
        ("season_id", "1675"),
        ("date_from", today),
        ("date_to", tomorrow),
    )
    EGYmatches = json.loads(get('https://app.sportdataapi.com/api/v1/soccer/matches',
                                headers=headers, params=params).text)["data"]

    # ------------------------------------------------------------------
    context = {
        'user': user,
        'friends': friends,
        'allposts': allposts,
        'postform': mypostform,
        'groups': groups,
        'newgroupform': newgroupform,
        'EGYmatches': EGYmatches,



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
        'user': user,

    }
    return render(request, 'Homepage/savedposts.html', context)
