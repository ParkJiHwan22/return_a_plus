from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create' ),
    path('<int:posts_pk>/', views.detail, name='detail' ),
    path('<int:posts_pk>/delete/', views.delete, name='delete' ),
    path('<int:posts_pk>/update/', views.update, name='update' ),
    path('<int:posts_pk>/review/', views.review_create, name='review_create'),
    path(
        '<int:posts_pk>/review/<int:review_pk>/delete/',
        views.review_delete,
        name='review_delete',
    ),
    path('<int:post_pk>/like/', views.like, name='like'),
    path('Our_Service/', views.Our_Service, name='Our_Service'),
    path('<str:city>/filter/', views.filter, name='filter'),
]
