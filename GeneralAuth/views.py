from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import *


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Authenticate the user and log them in
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Set the session expiration based on the "remember me" checkbox
                if form.cleaned_data['remember_me']:
                    request.session.set_expiry(settings.SESSION_COOKIE_AGE)
                else:
                    request.session.set_expiry(0)
                return redirect('index')
            else:
                # Handle invalid login
                return redirect('login')
    else:
        form = LoginForm()
    return render(request, 'GeneralAuth/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            role = form.cleaned_data['role']

            # Check if the username already exists
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'Username is already taken')
            else:
                # Create the user
                user = User.objects.create_user(username=username, email=email, password=password)

                # Add the user to the appropriate group
                group = Group.objects.get(name=role)
                user.groups.add(group)

                # Authenticate and login the user
                user = authenticate(username=username, password=password)
                login(request, user)

                return redirect('index')
    else:
        form = RegistrationForm()

    return render(request, 'GeneralAuth/register.html', {'form': form})
