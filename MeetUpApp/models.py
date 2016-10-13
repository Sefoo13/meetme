from __future__ import unicode_literals

from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserDetails(models.Model):
    full_name = models.CharField(max_length=100)
    country = models.CharField(max_length=50, default="Not set")
    city = models.CharField(max_length=50, default="Not set")
    birthday = models.DateField(max_length=50, default=datetime.now())
    rating = models.IntegerField(default=0)
    description = models.TextField(default="Not set")
    user = models.OneToOneField(User)

class Meetings(models.Model):
    text = models.TextField
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    date_arrive = models.DateField
    date_leave = models.DateField
    user = models.ForeignKey(User)


