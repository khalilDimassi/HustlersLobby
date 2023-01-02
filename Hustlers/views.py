from django.shortcuts import render


# Create your views here.
def create_profile_view(request):
    return render(request, 'Hustlers/create_profile.html')


def profile_view(request):
    return render(request, 'Hustlers/profile.html')
