# Generated by Django 4.1.4 on 2023-01-03 22:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Clients', '0004_clientjob_date_completed_clientjob_is_available_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_comment', to='Clients.clientjob')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_job_comment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
