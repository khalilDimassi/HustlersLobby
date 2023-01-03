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
            new_profile = HustlerProfile.objects.create(
                user_id=request.user.id,
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                profession=form.cleaned_data['profession'],
                establishment=form.cleaned_data['establishment'],
                birth_date=form.cleaned_data['birth_date'],
                profile_picture=form.cleaned_data['profile_picture'],
                bio=form.cleaned_data['bio'],
                phone_number=form.cleaned_data['phone_number'],
                skills=form.cleaned_data['skills'],
                languages=form.cleaned_data['languages'],
                fb_link=form.cleaned_data['fb_link'],
                tw_link=form.cleaned_data['tw_link'],
                gh_link=form.cleaned_data['gh_link'],
                li_link=form.cleaned_data['li_link'],
                ig_link=form.cleaned_data['ig_link'],
                pi_link=form.cleaned_data['pi_link'],
                pp_link=form.cleaned_data['pp_link'],
            )
            new_profile.save()
            # form.save()
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
