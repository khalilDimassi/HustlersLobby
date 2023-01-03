from django.contrib import admin

from .models import ClientProfile, ClientJob

# Register your models here.
admin.site.register(ClientProfile)
admin.site.register(ClientJob)
