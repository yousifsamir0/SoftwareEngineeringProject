from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreatForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def signup_v(request):
    form = UserCreatForm()
    if request.method == 'POST':
        form = UserCreatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Accounts:login')
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)


def login_v(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Profile:myprofile')
        else:
            messages.info(request, 'Username or password is incorrect.')
    context = {}
    return render(request, 'accounts/login.html', context)


def logout_v(request):
    logout(request)
    return redirect('Accounts:login')
