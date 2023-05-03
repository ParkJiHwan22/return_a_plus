from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Review
from .forms import PostForm, ReviewForm
from django.db.models import Count
import googlemaps


# Create your views here.
def index(request):
    posts = Post.objects.all()
    post_likes = [post.like_users.count() for post in posts]
    total_likes = sum(post_likes)
    ratios = [like_count / total_likes for like_count in post_likes]
    context = {
        'posts': posts,
        'post_likes': post_likes,
        'ratios': ratios,
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
        'form':form
    }
    return render(request, 'posts/create.html', context)


def detail(request, posts_pk):
    post = Post.objects.get(pk=posts_pk)
    reviews = post.review_set.all()
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
        'location':location
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

def about_us(request):
    return render(request, 'posts/about_us.html')
