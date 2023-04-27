from django.db import models
from django.conf import settings

class Post(models.Model):
    name = models.CharField(max_length=140)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')
    description = models.TextField()
    country = models.TextField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=80)
    post_image = models.ImageField(blank=True)


class Review(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.TextField()
    accuracy = models.IntegerField() 
    communication = models.IntegerField() 
    cleaniness = models.IntegerField() 
    location = models.IntegerField() 
    check_in = models.IntegerField() 
    value = models.IntegerField() 
    review_image = models.ImageField(blank=True)
    