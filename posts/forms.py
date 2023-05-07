from django import forms
from .models import Post, Review, PostImage, ReviewImage


POST_ADDRESS_CHOICES = (
    ("", "도시를 선택해주세요"),
    ("강릉", "강릉"),("강원", "강원"),("광주", "광주"),
    ("경기", "경기"),("경남", "경남"),("경북", "경북"),
    ("경주", "경주"),("대구", "대구"),("대전", "대전"),
    ("부산", "부산"),("서울", "서울"),("속초", "속초"),
    ("여수", "여수"),("인천", "인천"),("전남", "전남"),
    ("전북", "전북"),("전주", "전주"),("제주", "제주"),
    ("충남", "충남"),("충북", "충북"),
    # ('직접 입력', '직접 입력'),
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
        widget=forms.Select(
            choices = POST_ADDRESS_CHOICES,
            attrs={
                'class' : "form-select",
                'id' : "floatingSelect",
                'aria-label': "Floating label select example",
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

    # post_image = forms.ImageField(
    #     label='이미지 넣기',
    #     required=False,
    # )


    checkbox1 = forms.BooleanField(required=False, label='문화 및 역사 유적지', widget=forms.CheckboxInput(attrs={'style': 'transform: scale(1.3); cursor: pointer;'}))
    checkbox2 = forms.BooleanField(required=False, label='자연 경관', widget=forms.CheckboxInput(attrs={'style': 'transform: scale(1.3); cursor: pointer;'}))
    checkbox3 = forms.BooleanField(required=False, label='테마파크', widget=forms.CheckboxInput(attrs={'style': 'transform: scale(1.3); cursor: pointer;'}))
    checkbox4 = forms.BooleanField(required=False, label='어드벤처 및 스포츠', widget=forms.CheckboxInput(attrs={'style': 'transform: scale(1.3); cursor: pointer;'}))
    checkbox5 = forms.BooleanField(required=False, label ='축제 및 이벤트', widget=forms.CheckboxInput(attrs={'style': 'transform: scale(1.3); cursor: pointer;'}))
    checkbox6 = forms.BooleanField(required=False, label='먹거리', widget=forms.CheckboxInput(attrs={'style': 'transform: scale(1.3); cursor: pointer;'}))
    checkbox7 = forms.BooleanField(required=False, label='쇼핑', widget=forms.CheckboxInput(attrs={'style': 'transform: scale(1.3); cursor: pointer;'}))
    checkbox8 = forms.BooleanField(required=False, label='가족 나들이', widget=forms.CheckboxInput(attrs={'style': 'transform: scale(1.3); cursor: pointer;'}))
    checkbox9 = forms.BooleanField(required=False, label='데이트 코스', widget=forms.CheckboxInput(attrs={'style': 'transform: scale(1.3); cursor: pointer;'}))
    checkbox10 = forms.BooleanField(required=False, label = '인생샷 명소', widget=forms.CheckboxInput(attrs={'style': 'transform: scale(1.3); cursor: pointer;'}))
    
    
    
    class Meta:
        model = Post
        fields = (
            # "post_image",
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
        
    def save(self, commit=True):
        instance = super().save(commit)
        if self.cleaned_data.get('images'):
            for image in self.cleaned_data.get('images'):
                PostImage.objects.create(post=instance, image=image)
        return instance

class PostImageForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ('image',)
        widgets = {'image': forms.FileInput(attrs={'multiple': True})}
    

REVIEW_POINT_CHOICES = (
    ('', "점수를 선택해주세요"),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)


class ReviewForm(forms.ModelForm):
    accessibility = forms.CharField(
        label='접근성',
        widget=forms.Select(choices = REVIEW_POINT_CHOICES,
            attrs={
                'class' : "form-select",
            }
        ),
        required=False,
    )
    
    cost = forms.CharField(
        label='비용',
        widget=forms.Select(choices = REVIEW_POINT_CHOICES,
            attrs={
                'class' : "form-select",
            }
        ),
        required=False,
    )


    service = forms.CharField(
        label='서비스',
        widget=forms.Select(choices = REVIEW_POINT_CHOICES,
            attrs={
                'class' : "form-select",
            }
        ),
        required=False,
    )
    
            
    convenience_facilities = forms.CharField(
        label='편의시설',
        widget=forms.Select(
                   choices = REVIEW_POINT_CHOICES,
            attrs={
                'class' : "form-select",
            }
        ),
        required=False,
    )
    
    
    satisfaction = forms.CharField(
        label='만족도',
        widget= forms.Select(
            choices = REVIEW_POINT_CHOICES,
            attrs={
                'class' : "form-select",
            }
        ),
        required=False,
    )

    review = forms.CharField(
        label= '리뷰',
        widget= forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': 5,
            }
        ),
        required=False,
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
        )
        
    def save(self, commit=True):
        instance = super().save(commit)
        if self.cleaned_data.get('images'):
            for image in self.cleaned_data.get('images'):
                ReviewImage.objects.create(post=instance, image=image)
        return instance
        
class ReviewImageForm(forms.ModelForm):
    class Meta:
        model = ReviewImage
        fields = ('image',)
        widgets = {
            'image': forms.FileInput(attrs={'multiple': True}),
        }
                  

    