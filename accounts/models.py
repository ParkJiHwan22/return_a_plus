from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    nickname = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, blank=True)
    followings = models.ManyToManyField('self', related_name='followers', symmetrical=False)
    profile_image = models.ImageField(upload_to='profile_image/%Y/%m/%d/', blank=True)
    status_message = models.CharField(max_length=200, blank=True)
