from django.shortcuts import render
from .models import Profile


# Create your views here.


def profile(request):
    profile_obj = Profile.objects.get(user=request.user)

    # if i will send more than one obj to template i will send 1 dict !!!!!!!!!!

    return render(request, 'profile/testprof.html', {'profile': profile_obj})
