from django.urls import path

from . import views

app_name = 'Hustlers'

urlpatterns = [
    path('create-profile/', views.create_profile_view, name='create-profile'),
    path('profile/<int:pk>/', views.profile_view, name='profile'),
    path('profile/<int:pk>/edit/', views.edit_profile_view, name='edit-profile'),

    # TODO: Dashboard
    # path('dashboard/', views.dashboard_view, name='dashboard'),

    path('available-jobs/', views.available_jobs_view, name='available-jobs'),
    path('job-apply/<int:pk>/', views.job_apply_view, name='job-apply'),
    path('applied-team/<int:pk>/', views.applied_team_view, name='applied-team'),
    path('job-cancel/<int:pk>/', views.job_cancel_view, name='job-cancel'),

    # TODO: My jobs
    # path('my-jobs/', views.my_jobs_view, name='my-jobs'),

    # TODO: My job details
    # path('my-job-details/<int:pk>/', views.my_job_details_view, name='my-job-details'),

    # TODO: Recruit team request
    # path('recruit-team-request/<int:pk>/', views.recruit_team_request_view, name='recruit-team-request'),

    # TODO: Available teams
    # path('available-teams/', views.available_teams_view, name='available-teams'),

    # TODO: Team details
    # path('team-details/<int:pk>/', views.team_details_view, name='team-details'),
]
