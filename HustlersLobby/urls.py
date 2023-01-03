from django.conf import settings
from django.conf.urls.static import static, serve
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('CoreApp.urls')),
    path('accounts/', include('GeneralAuth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('contenttypes/', include('django.contrib.contenttypes.urls')),  # This is for the admin site
    path('client/', include('Clients.urls', namespace='client')),
    path('hustler/', include('Hustlers.urls',  namespace='hustler')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
