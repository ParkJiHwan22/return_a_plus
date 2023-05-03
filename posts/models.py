from django.db import models
from django.conf import settings

class Post(models.Model):
    name = models.CharField(max_length=140)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')
    description = models.TextField()
    city = models.CharField(max_length=80)
    price = models.IntegerField(null=True)
    address = models.CharField(max_length=80)
    post_image = models.ImageField(blank=True, upload_to='post_images/')


class Review(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.TextField()
    accessibility = models.IntegerField(null=True) 
    cost = models.IntegerField() 
    service = models.IntegerField() 
    convenience_facilities = models.IntegerField() 
    satisfaction = models.CharField(max_length=100)
    review_image = models.ImageField(blank=True, upload_to='review_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    