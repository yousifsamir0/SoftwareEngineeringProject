from django.shortcuts import render,redirect
from .models import Profile
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/login/')
def myprofile(request):
    slug=Profile.objects.get(user=request.user).slug
    return redirect('http://127.0.0.1:8000/Profiles/'+slug)


def profile(request,slug='myprofile'):
    
    profile_obj = Profile.objects.get(slug=slug)

    # if i will send more than one obj to template i will send 1 dict !!!!!!!!!!

    return render(request, 'profile/profile.html', {'profile': profile_obj})
