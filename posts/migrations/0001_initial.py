# Generated by Django 3.2.18 on 2023-05-03 05:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('description', models.TextField()),
                ('city', models.CharField(max_length=80)),
                ('price', models.IntegerField(null=True)),
                ('address', models.CharField(max_length=80)),
                ('post_image', models.ImageField(blank=True, upload_to='post_images/')),
                ('like_users', models.ManyToManyField(related_name='like_posts', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('accessibility', models.IntegerField(null=True)),
                ('cost', models.IntegerField()),
                ('service', models.IntegerField()),
                ('convenience_facilities', models.IntegerField()),
                ('satisfaction', models.IntegerField()),
                ('review_image', models.ImageField(blank=True, upload_to='review_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
