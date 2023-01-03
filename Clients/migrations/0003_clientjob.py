# Generated by Django 4.1.4 on 2023-01-03 18:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0002_alter_clientprofile_bio_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=2000)),
                ('budget', models.IntegerField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_due', models.DateTimeField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_job', to='Clients.clientprofile')),
            ],
        ),
    ]