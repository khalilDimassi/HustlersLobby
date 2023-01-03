from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client_profile')

    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    profession = models.CharField(max_length=100, null=True, blank=True)
    establishment = models.CharField(max_length=100, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True, default=timezone.now)
    profile_picture = models.ImageField(upload_to='imgs/profile_imgs', null=True, blank=True)
    bio = models.TextField(max_length=2000, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    fb_link = models.CharField(max_length=200, null=True, blank=True)
    tw_link = models.CharField(max_length=200, null=True, blank=True)
    gh_link = models.CharField(max_length=200, null=True, blank=True)
    li_link = models.CharField(max_length=200, null=True, blank=True)
    ig_link = models.CharField(max_length=200, null=True, blank=True)
    pi_link = models.CharField(max_length=200, null=True, blank=True)
    pp_link = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.user.username
