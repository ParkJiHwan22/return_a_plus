from django.db import models
from django.conf import settings
from accounts.models import User
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class Post(models.Model):
    name = models.CharField(max_length=140)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')
    description = models.TextField()
    city = models.CharField(max_length=80)
    price = models.IntegerField(null=True)
    address = models.CharField(max_length=80)
    post_image = models.ImageField(blank=True, upload_to='post_images/')
    views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    

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


    def __str__(self):
        return self.name


class PostImage(models.Model):
    def default_image():
        return "default_image_path.jpg"
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='post_images')
    image = ProcessedImageField(
        upload_to='posts/images',
        processors=[ResizeToFill(900, 900)],
        format='JPEG',
        options={'quality': 90},
        default=default_image,
    )
    
    def __str__(self):
        return f'{self.post.name} - {self.id}'

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
    

    
class ReviewImage(models.Model):
    def default_image():
        return "default_image_path.jpg"
    review = models.ForeignKey(to='posts.Review', on_delete=models.CASCADE, related_name='review_images')
    image = ProcessedImageField(
        upload_to='reviews/images',
        processors=[ResizeToFill(600, 600)],
        format='JPEG',
        options={'quality': 90},
        default=default_image,
        blank=True,
        null=True,
    )