from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View

from Clients.models import ClientJob
from Hustlers.forms import HustlerProfileForm
from Hustlers.models import HustlerProfile


def profile_view(request, pk):
    """
    get profile
    :param request: request
    :param pk: profile id
    :return: profile
    """
    user = get_object_or_404(User, pk=pk)
    hustler_profiles = HustlerProfile.objects.filter(user=user)
    if not hustler_profiles.exists():
        return redirect('Hustlers:create-profile')
    hustler_profile = hustler_profiles.first()
    context = {'hustler_profile': hustler_profile}
    return render(request, 'hustlers/profile.html', context)


def create_profile_view(request):
    """
    create profile
    :param request: request
    :return: create profile form
    """
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
    """
    edit profile
    :param request: request
    :param pk: profile id
    :return: edit profile form
    """
    hustler_profile = get_object_or_404(HustlerProfile, user_id=pk)
    if request.method == 'POST':
        form = HustlerProfileForm(request.POST, request.FILES, instance=hustler_profile)
        if form.is_valid():
            form.save()
            return redirect('Hustlers:profile', pk=request.user.pk)
    else:
        form = HustlerProfileForm(instance=hustler_profile)

    return render(request, 'hustlers/edit_profile.html', {'form': form})


def available_jobs_view(request):
    """
    get all jobs that are not assigned to any hustler
    :param request:
    :return: list of jobs that are available
    """
    jobs = HustlerProfile.objects.filter(is_available=True)
    return render(request, 'Clients/Jobs/view_jobs.html', {'jobs': jobs})


def job_apply_view(request, pk):
    """
    apply for a job
    :param request:
    :param pk: job id
    :return: job details
    """
    job = ClientJob.objects.get(pk=pk)
    job.is_taken = True
    job.applied_team.add(request.user.hustler_profile)
    job.save()
    return render(request, 'Clients/Jobs/view_job.html', {'clientjob': job, 'pk': pk})


def applied_team_view(request, pk):
    """
    Display the applied team for a specific job
    :param request:
    :param pk: job id
    :return: applied team for the specific job
    """
    job = get_object_or_404(ClientJob, pk=pk)
    applied_team = job.applied_team.all()  # Get the applied team for the specific job
    return render(request, 'Clients/Jobs/applied_team.html', {'applied_team': applied_team, 'job': job, 'pk': pk})


def job_cancel_view(request, pk):
    """
    Cancel a job
    :param request:
    :param pk: job id
    :return: job details
    """
    job = ClientJob.objects.get(pk=pk)
    if job.applied_team.count() == 1:
        job.is_taken = False
    job.applied_team.remove(request.user.hustler_profile)
    job.save()
    return render(request, 'Clients/Jobs/view_job.html', {'clientjob': job, 'pk': pk})
