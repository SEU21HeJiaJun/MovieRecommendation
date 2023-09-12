from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=255)
    cover_url = models.CharField(max_length=255)
    score = models.CharField(max_length=255)
    types = models.CharField(max_length=255)
    regions = models.CharField(max_length=255)
    release_date = models.CharField(max_length=255)
    actors = models.TextField()
    uid = models.ManyToManyField(User)