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
            new_profile = ClientProfile.objects.create(
                user_id=request.user.id,
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                profession=form.cleaned_data['profession'],
                establishment=form.cleaned_data['establishment'],
                birth_date=form.cleaned_data['birth_date'],
                profile_picture=form.cleaned_data['profile_picture'],
                bio=form.cleaned_data['bio'],
                phone_number=form.cleaned_data['phone_number'],
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
