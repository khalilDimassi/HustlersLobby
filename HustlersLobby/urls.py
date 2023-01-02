from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('CoreApp.urls')),
    path('accounts/', include('GeneralAuth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('contenttypes/', include('django.contrib.contenttypes.urls')),
]
