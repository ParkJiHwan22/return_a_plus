from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Review
from accounts.models import User
from .forms import PostForm, ReviewForm
from django.db.models import Count
import googlemaps
from django.contrib.auth import get_user_model

colors = [
    'rgba(255, 99, 132, 0.7)',
    'rgba(54, 162, 235, 0.7)',
    'rgba(255, 206, 86, 0.7)',
    'rgba(75, 192, 192, 0.7)',
    'rgba(153, 102, 255, 0.7)',
    'rgba(255, 159, 64, 0.7)',
    'rgba(123, 104, 238, 0.7)',
    'rgba(255, 250, 205, 0.7)',
    'rgba(128, 0, 0, 0.7)',
    'rgba(0, 128, 0, 0.7)',
    'rgba(0, 0, 128, 0.7)',
    'rgba(255, 215, 0, 0.7)',
    'rgba(255, 105, 180, 0.7)',
    'rgba(0, 255, 255, 0.7)',
    'rgba(218, 165, 32, 0.7)',
    'rgba(128, 128, 0, 0.7)',
    'rgba(75, 0, 130, 0.7)',
    'rgba(165, 42, 42, 0.7)',
    'rgba(0, 128, 128, 0.7)',
    'rgba(139, 69, 19, 0.7)',
    'rgba(25, 25, 112, 0.7)',
    'rgba(0, 255, 0, 0.7)',
    'rgba(255, 20, 147, 0.7)',
]

color_dict = {}
color_index = 0


# Create your views here.
def index(request):
    global color_index
    posts = Post.objects.all()
    post_likes = [post.like_users.count() for post in posts]
    total_likes = sum(post_likes)
    ratios = []
    likes_order_posts = Post.objects.annotate(like_count=Count('like_users')).order_by('-like_count')
    posts_with_images = likes_order_posts.exclude(post_image__exact='')
    if total_likes > 0:
        ratios = [like_count / total_likes for like_count in post_likes]
    for post in posts:
        if post.address not in color_dict:
            color_dict[post.address] = colors[color_index]
            color_index += 1

    color_list = [color_dict[post.address] for post in posts]
    
    context = {
        'posts': posts,
        'post_likes': post_likes,
        'ratios': ratios,
        'color_dict': color_dict, 
        'color_list': color_list,
        'posts_with_images': posts_with_images,
    }
    return render(request, 'posts/index.html', context)


@login_required
def create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:index')
    else:
        form = PostForm()
    context = {
        'form':form,
    }
    return render(request, 'posts/create.html', context)


def detail(request, posts_pk):
    post = Post.objects.get(pk=posts_pk)
    reviews = post.review_set.all()
    users = get_user_model()
    person = User.objects.get(username=request.user)
    review_form = ReviewForm(request.POST, request.FILES)
    my_key = "AIzaSyAd9M3rcxiyzS9IxbErxaMv45mw94kQFxY"
    maps = googlemaps.Client(key=my_key)
    places = [post.address]
    print(places)
    geo_location = maps.geocode(places)[0].get('geometry')
    location = geo_location['location']
    print(location)
    context = {
        'post': post,
        'review_form': review_form,
        'reviews': reviews,
        'location':location,
        'person':person,
    }
    return render(request, 'posts/detail.html', context,)


@login_required
def delete(request, posts_pk):
    post = Post.objects.get(pk=posts_pk)
    if post.user == request.user:
        post.delete()
    return redirect('posts:index')


@login_required
def update(request, posts_pk):
    post = Post.objects.get(pk=posts_pk)
    if post.user == request.user:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                return redirect('posts:detail', post.pk)
        form = PostForm(instance=post)
        context = {
            'post': post,
            'form': form,
        }
        return render(request, 'posts/update.html', context)
    else:
        return redirect('posts:detail', post.pk)


@login_required
def review_create(request, posts_pk):
    post = Post.objects.get(pk=posts_pk)
    review_form = ReviewForm(request.POST, request.FILES)
    if review_form.is_valid():
        review = review_form.save(commit=False)
        review.user = request.user
        review.post = post
        review.save()
        return redirect('posts:detail', post.pk)
    context = {
        'post': post,
        'review_form': review_form,
    }
    return render(request, 'posts/detail.html', context)


@login_required
def review_delete(request, posts_pk, review_pk):
    review = Review.objects.get(pk=review_pk)
    if review.user == request.user:
        review.delete()
    return redirect('posts:detail', posts_pk)

@login_required
def like(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.user in post.like_users.all():
        post.like_users.remove(request.user)
    else:
        post.like_users.add(request.user)
    return redirect('posts:index')


def Our_Service(request):
    return render(request, 'posts/Our_Service.html')

