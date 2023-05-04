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
    
    price = forms.CharField(
        label='가격(성인 기준)',
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


    checkbox1 = forms.BooleanField(required=False, label='문화 및 역사 유적지')
    checkbox2 = forms.BooleanField(required=False, label='자연 경관')
    checkbox3 = forms.BooleanField(required=False, label='테마파크')
    checkbox4 = forms.BooleanField(required=False, label='어드벤처 및 스포츠')
    checkbox5 = forms.BooleanField(required=False, label ='축제 및 이벤트')
    checkbox6 = forms.BooleanField(required=False, label='먹거리')
    checkbox7 = forms.BooleanField(required=False, label='쇼핑')
    checkbox8 = forms.BooleanField(required=False, label='가족 나들이')
    checkbox9 = forms.BooleanField(required=False, label='데이트 코스')
    checkbox10 = forms.BooleanField(required=False, label = '셀카 명소')
    
    
    
    class Meta:
        model = Post
        fields = (
            "post_image",
            "name",
            "city",
            "address",
            "price", 
            "description",
            "checkbox1",
            "checkbox2",
            "checkbox3",
            "checkbox4",
            "checkbox5",
            "checkbox6",
            "checkbox7",
            "checkbox8",
            "checkbox9",
            "checkbox10",
        )
        
        widgets = {
            'checkbox1': forms.CheckboxInput(),
            'checkbox2': forms.CheckboxInput(),
            'checkbox3': forms.CheckboxInput(),
            'checkbox4': forms.CheckboxInput(),
            'checkbox5': forms.CheckboxInput(),
            'checkbox6': forms.CheckboxInput(),
            'checkbox7': forms.CheckboxInput(),
            'checkbox8': forms.CheckboxInput(),
            'checkbox9': forms.CheckboxInput(),
            'checkbox10': forms.CheckboxInput(),
        }

    

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