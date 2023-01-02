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
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            profession = form.cleaned_data['profession']
            establishment = form.cleaned_data['establishment']
            birth_date = form.cleaned_data['birth_date']
            profile_picture = form.cleaned_data['profile_picture']
            bio = form.cleaned_data['bio']

            # Create a new ClientProfile instance
            client_profile = ClientProfile.objects.create(
                user=request.user,
                first_name=first_name,
                last_name=last_name,
                profession=profession,
                establishment=establishment,
                birth_date=birth_date,
                profile_picture=profile_picture,
                bio=bio,
            )

            return redirect('index')
    else:
        form = ClientProfileForm()

    return render(request, 'Clients/create_profile.html', {'form': form})
