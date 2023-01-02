from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client_profile')

    first_name = models.CharField(max_length=30, default='First Name')
    last_name = models.CharField(max_length=30, default='Last Name')
    profession = models.CharField(max_length=100, default='Profession')
    establishment = models.CharField(max_length=100, default='Establishment')
    birth_date = models.DateField(null=True, blank=True, default=timezone.now)
    profile_picture = models.ImageField(upload_to='imgs/profile_imgs', default='GeneralAuth/imgs/dpfp/default_pic.png')
    bio = models.TextField(max_length=500, default='Bio')
