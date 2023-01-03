from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404

from Clients.forms import ClientProfileForm, ClientJobForm
from Clients.models import ClientProfile, ClientJob


# Profile views
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


# Jobs views
def view_jobs_view(request):
    context = {
        'jobs': ClientJob.objects.all()
    }
    return render(request, 'Clients/Jobs/view_jobs.html', context)


def view_job_view(request, pk):
    context = {
        'job': ClientJob.objects.get(pk=pk)
    }
    return render(request, 'Clients/Jobs/view_job.html', context)


def view_client_jobs_view(request, pk):
    context = {
        'jobs': ClientJob.objects.filter(client_id=pk)
    }
    return render(request, 'Clients/Jobs/view_jobs.html', context)


def post_job_view(request):
    if request.method == 'POST':
        form = ClientJobForm(request.POST, request.FILES)

        if form.is_valid():
            new_job = ClientJob.objects.create(
                client_id=request.user.client_profile.pk,
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                budget=form.cleaned_data['budget'],
            )
            new_job.save()
            return redirect('client:view-jobs')
    else:
        form = ClientJobForm()

    return render(request, 'Clients/Jobs/post_job.html', {'form': form})


def edit_job_view(request, pk):
    job = get_object_or_404(ClientJob, pk=pk)
    if request.method == 'POST':
        form = ClientJobForm(request.POST, request.FILES, instance=job)

        if form.is_valid():
            form.save()
            return redirect('client:view-job', pk=pk)
    else:
        form = ClientJobForm(instance=job)

    return render(request, 'Clients/Jobs/edit_job.html', {'form': form})


def cancel_job_view(request, pk):
    job = get_object_or_404(ClientJob, pk=pk)
    job.is_available = False
    job.save()
    return redirect('client:view-jobs')

