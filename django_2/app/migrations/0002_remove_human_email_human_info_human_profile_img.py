# Generated by Django 4.0.5 on 2022-06-23 11:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='human',
            name='email',
        ),
        migrations.AddField(
            model_name='human',
            name='info',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='human',
            name='profile_img',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='media/user-img/'),
            preserve_default=False,
        ),
    ]
