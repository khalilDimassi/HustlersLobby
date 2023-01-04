from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'Clients'

urlpatterns = [
    # TODO: Landing page
    # path('', views.landing_page_view, name='landing-page'),

    # profile urls
    path('create-profile/', views.create_profile_view, name='create-profile'),
    path('profile/<int:pk>/', views.profile_view, name='profile'),
    path('profile/<int:pk>/edit/', views.edit_profile_view, name='edit-profile'),

    # job urls
    path('post-job/', views.post_job_view, name='post-job'),
    path('edit-job/<int:pk>/', views.edit_job_view, name='edit-job'),
    path('cancel-job/<int:pk>/', views.cancel_job_view, name='cancel-job'),
    path('view-job/<int:pk>/', views.ViewJobView.as_view(), name='view-job'),
    path('view-jobs/', views.view_jobs_view, name='view-jobs'),
    path('view-client-jobs/<int:pk>/', views.view_client_jobs_view, name='view-client-jobs'),

    # TODO: follow advancement of accepted jobs
    # path('view-accepted-jobs/', views.view_accepted_jobs_view, name='view-accepted-jobs'),

    # TODO : detailed advencement of accepted job
    # path('view-accepted-job/<int:pk>/', views.view_accepted_job_view, name='view-accepted-job'),

    # TODO: Hire a hustler
    # path('hire-hustler/', views.hire_hustler_view, name='hire-hustler'),

]
