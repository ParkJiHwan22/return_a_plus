from django import forms
from .models import Post, Review

class PostForm(forms.ModelForm):
    name = forms.CharField(
        label='숙소 명',
        widget= forms.TextInput(
            attrs= {
                'class': 'form-control'
            }
        )
    )

    address = forms.CharField(
        label='숙소 주소',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    description = forms.CharField(
        label= '숙소 설명',
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
            "address", 
            "description",  
        )


REVIEW_POINT_CHOICES = (
        ("★☆☆☆☆ (1/5)", "★☆☆☆☆ (1/5)"),
        ("★★☆☆☆ (2/5)", "★★☆☆☆ (2/5)"),
        ("★★★☆☆ (3/5)", "★★★☆☆ (3/5)"),
        ("★★★★☆ (4/5)", "★★★★☆ (4/5)"),
        ("★★★★★ (5/5)", "★★★★★ (5/5)"),
)


class ReviewForm(forms.ModelForm):
    satisfaction = forms.CharField(
        label='점수',
        widget= forms.Select(choices=REVIEW_POINT_CHOICES)
    )


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
