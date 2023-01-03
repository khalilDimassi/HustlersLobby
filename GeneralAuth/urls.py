from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('settings/<int:pk>/edit/', views.edit_settings_view, name='edit-settings'),
    path('settings/<int:pk>/password/', views.edit_password_view, name='edit-password'),

    # TODO: Delete account
    # path('settings/<int:pk>/delete/', views.delete_account_view, name='delete-account'),

    # TODO: Reset password
    # path('reset-password/', views.reset_password_view, name='reset-password'),
]
