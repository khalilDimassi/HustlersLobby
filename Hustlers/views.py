from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404

from Hustlers.forms import HustlerProfileForm
from Hustlers.models import HustlerProfile


def profile_view(request, pk):
    user = get_object_or_404(User, pk=pk)
    hustler_profiles = HustlerProfile.objects.filter(user=user)
    if not hustler_profiles.exists():
        return redirect('Hustlers:create-profile')
    hustler_profile = hustler_profiles.first()
    context = {'hustler_profile': hustler_profile}
    return render(request, 'hustlers/profile.html', context)


def create_profile_view(request):
    if request.method == 'POST':
        form = HustlerProfileForm(request.POST, request.FILES)
        if form.is_valid():
            # new_profile = HustlerProfile.objects.create(user=request.user)
            form.save()
            return redirect('Hustlers:profile', pk=request.user.pk)
    else:
        form = HustlerProfileForm()

    return render(request, 'hustlers/create_profile.html', {'form': form})


def edit_profile_view(request, pk):
    hustler_profile = get_object_or_404(HustlerProfile, user_id=pk)
    if request.method == 'POST':
        form = HustlerProfileForm(request.POST, request.FILES, instance=hustler_profile)
        if form.is_valid():
            form.save()
            return redirect('Hustlers:profile', pk=request.user.pk)
    else:
        form = HustlerProfileForm(instance=hustler_profile)

    return render(request, 'hustlers/edit_profile.html', {'form': form})
