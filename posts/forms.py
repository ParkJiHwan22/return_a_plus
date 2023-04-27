from django import forms
from .models import Post, Review

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            "name", 
            "description", 
            "country", 
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
            "accuracy", 
            "communication", 
            "cleaniness", 
            "location", 
            "check_in", 
            "value", 
            "review_image", 
        )
