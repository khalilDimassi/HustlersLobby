from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'Clients'

urlpatterns = [
    path('create-profile/', views.create_profile_view, name='create-profile'),
    path('profile/<int:pk>/', views.profile_view, name='profile'),
    path('profile/<int:pk>/edit/', views.edit_profile_view, name='edit-profile'),

]
