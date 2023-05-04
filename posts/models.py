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

    checkbox1 = models.BooleanField(default=False)
    checkbox2 = models.BooleanField(default=False)
    checkbox3 = models.BooleanField(default=False)
    checkbox4 = models.BooleanField(default=False)
    checkbox5 = models.BooleanField(default=False)
    checkbox6 = models.BooleanField(default=False)
    checkbox7 = models.BooleanField(default=False)
    checkbox8 = models.BooleanField(default=False)
    checkbox9 = models.BooleanField(default=False)
    checkbox10 = models.BooleanField(default=False)


class Review(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.TextField()
    accessibility = models.CharField(max_length=100)
    cost = models.CharField(max_length=100)
    service = models.CharField(max_length=100)
    convenience_facilities = models.CharField(max_length=100)
    satisfaction = models.CharField(max_length=100)
    review_image = models.ImageField(blank=True, upload_to='review_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    