from django.contrib import admin

from .models import ClientProfile, ClientJob, JobComment

# Register your models here.
admin.site.register(ClientProfile)
admin.site.register(ClientJob)
admin.site.register(JobComment)
