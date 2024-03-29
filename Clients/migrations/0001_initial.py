# Generated by Django 4.1.4 on 2023-01-02 15:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='First Name', max_length=30)),
                ('last_name', models.CharField(default='Last Name', max_length=30)),
                ('profession', models.CharField(default='Profession', max_length=100)),
                ('establishment', models.CharField(default='Establishment', max_length=100)),
                ('birth_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('profile_picture', models.ImageField(default='GeneralAuth/imgs/dpfp/default_pic.png', upload_to='imgs/profile_imgs')),
                ('bio', models.TextField(default='Bio', max_length=500)),
                ('phone_number', models.CharField(default='0000000000', max_length=20)),
                ('fb_link', models.URLField(default='Facebook Link')),
                ('tw_link', models.URLField(default='Twitter Link')),
                ('gh_link', models.URLField(default='Github Link')),
                ('li_link', models.URLField(default='LinkedIn Link')),
                ('ig_link', models.URLField(default='Instagram Link')),
                ('pi_link', models.URLField(default='Pinterest Link')),
                ('pp_link', models.URLField(default='website Link')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='client_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
