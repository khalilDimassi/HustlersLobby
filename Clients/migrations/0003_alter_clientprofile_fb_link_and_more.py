# Generated by Django 4.1.4 on 2023-01-03 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0002_alter_clientprofile_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientprofile',
            name='fb_link',
            field=models.URLField(blank=True, help_text='facebook link', null=True),
        ),
        migrations.AlterField(
            model_name='clientprofile',
            name='gh_link',
            field=models.URLField(blank=True, help_text='github link', null=True),
        ),
        migrations.AlterField(
            model_name='clientprofile',
            name='ig_link',
            field=models.URLField(blank=True, help_text='instagram link', null=True),
        ),
        migrations.AlterField(
            model_name='clientprofile',
            name='li_link',
            field=models.URLField(blank=True, help_text='linkedin link', null=True),
        ),
        migrations.AlterField(
            model_name='clientprofile',
            name='pi_link',
            field=models.URLField(blank=True, help_text='pinterest link', null=True),
        ),
        migrations.AlterField(
            model_name='clientprofile',
            name='pp_link',
            field=models.URLField(blank=True, help_text='personal website link', null=True),
        ),
        migrations.AlterField(
            model_name='clientprofile',
            name='tw_link',
            field=models.URLField(blank=True, help_text='twitter link', null=True),
        ),
    ]