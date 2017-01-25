from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Interest(models.Model):
    interest_name = models.CharField(max_length=255)


class User(models.Model):
    name = models.CharField(max_length=50)
    interest = models.ManyToManyField(Interest)
