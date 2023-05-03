from django import forms
from .models import Post, Review

class PostForm(forms.ModelForm):
    name = forms.CharField(
        label='관광지 이름',
        widget= forms.TextInput(
            attrs= {
                'class': 'form-control'
            }
        )
    )

    city = forms.CharField(
        label='도시',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    
    address = forms.CharField(
        label='관광지 주소',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    
    description = forms.CharField(
        label= '관광지 설명',
        widget= forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': 3,
            }
            
        )
    )

    post_image = forms.ImageField(
        label='이미지 넣기',
        required=False,
    )

    class Meta:
        model = Post
        fields = (
            "post_image",
            "name",
            "city",
            "address", 
            "description",  
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
