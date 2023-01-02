from django.urls import path

from . import views

app_name = 'Hustlers'

urlpatterns = [
    path('create-profile/', views.create_profile_view, name='create-profile'),
    path('profile/<int:pk>/', views.profile_view, name='profile'),

]
