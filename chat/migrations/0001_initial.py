# Generated by Django 3.1.1 on 2021-04-10 16:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomName', models.CharField(default='', max_length=20)),
                ('password', models.CharField(default='', max_length=20)),
                ('limit', models.IntegerField(default=0)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('which', models.CharField(default='private', max_length=20)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('blocked', models.ManyToManyField(related_name='blocked_users', to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(related_name='members_of_room', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-time'],
            },
        ),
        migrations.CreateModel(
            name='Chats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(default='', max_length=100)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('by_whom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='by_whom', to=settings.AUTH_USER_MODEL)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='which_room', to='chat.room')),
            ],
        ),
    ]
