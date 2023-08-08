# Generated by Django 3.1.1 on 2021-04-09 19:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0021_delete_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='views',
            field=models.ManyToManyField(blank=True, related_name='tot_views', to=settings.AUTH_USER_MODEL),
        ),
    ]
