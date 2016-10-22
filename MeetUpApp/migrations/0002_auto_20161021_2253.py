# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-21 22:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MeetUpApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='Not set', max_length=200)),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('date_arrive', models.DateField(auto_now=True)),
                ('date_leave', models.DateField(auto_now=True)),
                ('find_local', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='meetings',
            name='u',
        ),
        migrations.RemoveField(
            model_name='userdetails',
            name='u',
        ),
        migrations.AddField(
            model_name='userdetails',
            name='agree_to_meet',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='description',
            field=models.TextField(default='Not set'),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='full_name',
            field=models.CharField(default='Not set', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdetails',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='user',
            field=models.OneToOneField(default='dd', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='birthday',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='city',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='country',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.DeleteModel(
            name='Meetings',
        ),
    ]