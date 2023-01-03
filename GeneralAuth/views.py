from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth import logout
from django.contrib.auth.models import Group
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

                # Redirect to the user's profile page
                if role == 'Clients':
                    return redirect('client:profile', pk=user.pk)
                elif role == 'Hustlers':
                    return redirect('hustler:profile', pk=user.pk)
    else:
        form = RegistrationForm()

    return render(request, 'GeneralAuth/register.html', {'form': form})


def edit_settings_view(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditSettingsForm(request.POST, instance=request.user)
        if form.is_valid():
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.save()
            messages.success(request, 'Your settings have been successfully updated.')
            return redirect('index')  # Redirect to the user's profile page
    else:
        form = EditSettingsForm(
            initial={'username': user.username, 'email': user.email}, instance=request.user)
    return render(request, 'GeneralAuth/edit_settings.html', {'form': form})


def edit_password_view(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditPasswordForm(request.POST)  # A form bound to the POST DATA
        if form.is_valid():
            user.set_password(form.cleaned_data['password'])
            user.save()
            update_session_auth_hash(request, request.user)  # Important! Otherwise the user will be logged out
            messages.success(request, 'Your password has been successfully updated.')

            return redirect('index')
    else:
        form = EditPasswordForm()
    return render(request, 'GeneralAuth/edit_password.html', {'form': form})
