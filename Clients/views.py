from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404

from Clients.forms import ClientProfileForm
from Clients.models import ClientProfile


def profile_view(request, pk):
    user = get_object_or_404(User, pk=pk)
    client_profiles = ClientProfile.objects.filter(user=user)
    if not client_profiles.exists():
        return redirect('client:create-profile')
    client_profile = client_profiles.first()
    context = {'client_profile': client_profile}
    return render(request, 'clients/profile.html', context)


def create_profile_view(request):
    if request.method == 'POST':
        form = ClientProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('client:profile', pk=request.user.pk)
    else:
        form = ClientProfileForm()

    return render(request, 'Clients/create_profile.html', {'form': form})


def edit_profile_view(request, pk):
    client_profile = get_object_or_404(ClientProfile, user_id=pk)
    if request.method == 'POST':
        form = ClientProfileForm(request.POST, request.FILES, instance=client_profile)
        if form.is_valid():
            form.save()
            return redirect('client:profile', pk=request.user.pk)
    else:
        form = ClientProfileForm(instance=client_profile)

    return render(request, 'Clients/edit_profile.html', {'form': form})
