from django.shortcuts import render
from django.db.models import Q
from django.http import JsonResponse
from Profile.models import Profile
from Groups.models import Group
from Groups.forms import GroupForm
# Create your views here.


def search_view(request):
    if request.is_ajax():
        query = request.GET.get('query')

        return JsonResponse(context, status=200)


def searchpage(request, query):
    user = request.user
    newgroupform = GroupForm(request.POST or None, request.FILES or None)
    groups = user.profile.get_groups()
    Profiles = Profile.objects.filter(
        Q(fName__startswith=query) | Q(slug__icontains=query) | Q(
            eMail=query) | Q(fName__icontains=query))
    sgroups = Group.objects.filter(
        Q(name__startswith=query) | Q(description__icontains=query))

    context = {
        "profiles": Profiles,
        "user": user,
        "groups": groups,
        "newgroupform": newgroupform,
        "sgroups": sgroups,
    }
    return render(request, 'search/search.html', context)
