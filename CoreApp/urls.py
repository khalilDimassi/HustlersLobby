from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),  # TODO: missing footer and navbar links

    # TODO: Contact page
    # path('contact/', views.contact, name='contact'),

    # TODO: About page
    # path('about/', views.about, name='about'),

    # TODO: Blogs app
    # path('blogs/', include('blogs.urls')),

    # TODO: internal mail app
    # path('mail/', include('mail.urls')),

]
