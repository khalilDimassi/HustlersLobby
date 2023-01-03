from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'Clients'

urlpatterns = [
    path('create-profile/', views.create_profile_view, name='create-profile'),
    path('profile/<int:pk>/', views.profile_view, name='profile'),
    path('profile/<int:pk>/edit/', views.edit_profile_view, name='edit-profile'),
    # TODO: Landing page
    # path('', views.landing_page_view, name='landing-page'),

    # TODO: Post a job
    # path('post-job/', views.post_job_view, name='post-job'),

    # TODO: edit a job
    # path('edit-job/<int:pk>/', views.edit_job_view, name='edit-job'),

    # TODO: delete a job
    # path('delete-job/<int:pk>/', views.delete_job_view, name='delete-job'),

    # TODO: view a job
    # path('view-job/<int:pk>/', views.view_job_view, name='view-job'),

    # TODO: view all jobs
    # path('view-jobs/', views.view_jobs_view, name='view-jobs'),


    # TODO: Hire a hustler
    # path('hire-hustler/', views.hire_hustler_view, name='hire-hustler'),

]
