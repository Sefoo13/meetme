from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserDetails(models.Model):
    country = models.CharField(max_length= 50)
    city = models.CharField(max_length= 50)
    birthday = models.DateField(max_length= 50)
    rating = models.IntegerField
    description = models.TextField
    photo = models.ImageField
    u = models.ForeignKey(User)

class Meetings(models.Model):
    text = models.TextField
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    date = models.DateField
    u = models.ForeignKey(User)


