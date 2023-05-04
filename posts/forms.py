from django import forms
from .models import Post, Review

POST_ADDRESS_CHOICES = (
        ("서울", "서울"),("경기", "경기"),("대구", "대구"),
        ("부산", "부산"),("광주", "광주"),("대전", "대전"),
        ("인천", "인천"),("경기", "경기"),("충북", "충북"),
        ("충남", "충남"),("전북", "전북"),("전남", "전남"),
        ("경북", "경북"),("경남", "경남"),("제주", "제주"),
)



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

    category = forms.CharField(
        label="카테고리",
        widget=forms.Select(choices=POST_ADDRESS_CHOICES)
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
            "category", 
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
        label='만족도',
        widget= forms.Select(choices=REVIEW_POINT_CHOICES)
    )

    accessibility = forms.CharField(
        label='접근성',
        widget=forms.Select(choices=REVIEW_POINT_CHOICES)
    )

    service = forms.CharField(
        label='서비스',
        widget=forms.Select(choices=REVIEW_POINT_CHOICES)
    )

    convenience_facilities = forms.CharField(
        label='편의시설',
        widget=forms.Select(choices=REVIEW_POINT_CHOICES)
    )

    cost = forms.CharField(
        label='비용',
        widget=forms.Select(choices=REVIEW_POINT_CHOICES)
    )


    class Meta:
        model = Review
        fields = (
            "accessibility", 
            "cost", 
            "service", 
            "convenience_facilities", 
            "satisfaction",
            "review",
            "review_image", 
        )
