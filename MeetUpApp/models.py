from __future__ import unicode_literals

from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserDetails(models.Model):
    full_name = models.CharField(max_length=100)
    country = models.CharField(max_length=50, default="")
    city = models.CharField(max_length=50, default="")
    birthday = models.DateField(auto_now=True)
    rating = models.IntegerField(default=0)
    description = models.TextField(default="Not set")
    user = models.OneToOneField(User)
    agree_to_meet = models.BooleanField(default=False)

    def get_year(self):
        return self.birthday.year

    def get_month(self):
        return self.birthday.month

    def get_day(self):
        return self.birthday.day


class Trip(models.Model):
    description = models.CharField(max_length=500, default="Not set")
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    date_arrive = models.DateField(auto_now=True)
    date_leave = models.DateField(auto_now=True)
    find_local = models.BooleanField(default=False)
    user = models.ForeignKey(User)


