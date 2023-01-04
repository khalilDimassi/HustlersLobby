from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from django.views import generic

from Clients.forms import ClientProfileForm, ClientJobForm, AddCommentForm
from Clients.models import ClientProfile, ClientJob, JobComment


# Profile views
def profile_view(request, pk):
    """
    View for the client profile
    :param request: request object
    :param pk: user id
    :return: client profile
    """
    user = get_object_or_404(User, pk=pk)
    client_profiles = ClientProfile.objects.filter(user=user)
    if not client_profiles.exists():
        return redirect('client:create-profile')
    client_profile = client_profiles.first()
    context = {'client_profile': client_profile}
    return render(request, 'clients/profile.html', context)


def create_profile_view(request):
    """
    View for creating a client profile
    :param request:  request object
    :return:  client profile
    """
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
    """
    View for editing a client profile
    :param request:  request object
    :param pk:  user id
    :return: client profile
    """
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
    """
    View for viewing all jobs
    :param request: request object
    :return: all jobs
    """
    context = {
        'jobs': ClientJob.objects.all()
    }
    return render(request, 'Clients/Jobs/view_jobs.html', context)


class ViewJobView(generic.DetailView):
    """
    View for viewing a job details
    """
    model = ClientJob
    template_name = 'Clients/Jobs/view_job.html'
    form_class = AddCommentForm  # Add the form class

    def get_context_data(self, **kwargs):
        context = super(ViewJobView, self).get_context_data(**kwargs)  # Get the default context data
        context["form"] = self.form_class()  # Add the form to the context
        return context

    # commenting handler
    def post(self, request, *args, **kwargs):
        # Check if the request is for adding a new comment
        if "add-comment" in request.POST:
            form = self.form_class(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.job = self.get_object()
                comment.user = request.user
                comment.save()
                return redirect('Clients:view-job', pk=self.get_object().pk)

        # or editing an existing comment
        elif "edit-comment" in request.POST:
            comment_id = request.POST.get("comment_id")
            comment = get_object_or_404(JobComment, pk=comment_id)
            form = self.form_class(request.POST, instance=comment)

            if form.is_valid():
                form.instance.edited_at = timezone.now()
                form.instance.is_edited = True
                form.save()
                return redirect('Clients:view-job', pk=self.get_object().pk)

        return redirect('Clients:view-job', pk=self.get_object().pk)


def view_client_jobs_view(request, pk):
    """
    View for viewing all jobs posted by a client
    :param request: request object
    :param pk: client id
    :return: all jobs posted by a client
    """
    context = {
        'jobs': ClientJob.objects.filter(client_id=pk)
    }
    return render(request, 'Clients/Jobs/view_jobs.html', context)


def post_job_view(request):
    """
    View for posting a job
    :param request: request object
    :return: job details
    """
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
    """
    View for editing a job
    :param request: request object
    :param pk: job id
    :return: job details
    """
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
    """
    View for cancelling a job
    :param request: request object
    :param pk: job id
    :return: job details
    """
    job = get_object_or_404(ClientJob, pk=pk)
    job.is_available = False
    job.save()
    return redirect('client:view-jobs')


def accept_team_view(request, pk):
    """
    View for accepting a team assigned to a job
    :param request: request object
    :param pk: job id
    :return: job details
    """
    job = get_object_or_404(ClientJob, pk=pk)
    job.is_taken = True
    job.is_available = False
    job.save()
    return redirect('client:view-job', pk=pk)
