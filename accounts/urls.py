from django.urls import path, include
from . import views

app_name = 'accounts'
urlpatterns = [
    # 로그인, 로그아웃, 회원가입, 계정삭제, 정보수정, 비밀번호변경
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('password/', views.change_password, name='change_password'),
    # 팔로우
    path('<int:user_pk>/follow/', views.follow, name='follow'),
    path('profile/<username>/', views.profile, name='profile'),
    path('accounts/', include('allauth.urls'))
]
