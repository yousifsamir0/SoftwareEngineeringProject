from django.shortcuts import render, redirect
from Posts.models import Post, Comment
from Groups.models import Group
from Posts.forms import postform
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='/login/')
def Home(request):
    mypostform = postform(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if mypostform.is_valid():
            post = mypostform.save(commit=False)
            post.author = request.user.profile
            post.save()
            return redirect('Homepage:homepage')
    user = request.user
    friends = user.profile.get_friends()
    # --------------------get all related posts------------------------
    allposts = Post.objects.filter(author=user.profile)

    for friend in friends:
        friendposts = Post.objects.filter(author=friend.profile, group=None)
        allposts = allposts | friendposts
    # ------------------------------------------------------------------
    context = {
        'user': user,
        'friends': friends,
        'allposts': allposts,
        'postform': mypostform,
    }
    return render(request, 'Homepage/home.html', context)
