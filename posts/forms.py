from django import forms
from .models import Post, Review

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            "name", 
            "description",  
            "city", 
            "price", 
            "address", 
            "post_image",
        )


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = (
            "review",
            "accessibility", 
            "cost", 
            "service", 
            "convenience_facilities", 
            "satisfaction",
            "review_image", 
        )
