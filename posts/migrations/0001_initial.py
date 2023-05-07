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
                ('views', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('checkbox1', models.BooleanField(default=False)),
                ('checkbox2', models.BooleanField(default=False)),
                ('checkbox3', models.BooleanField(default=False)),
                ('checkbox4', models.BooleanField(default=False)),
                ('checkbox5', models.BooleanField(default=False)),
                ('checkbox6', models.BooleanField(default=False)),
                ('checkbox7', models.BooleanField(default=False)),
                ('checkbox8', models.BooleanField(default=False)),
                ('checkbox9', models.BooleanField(default=False)),
                ('checkbox10', models.BooleanField(default=False)),
                ('like_users', models.ManyToManyField(related_name='like_posts', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('accessibility', models.CharField(max_length=100)),
                ('cost', models.CharField(max_length=100)),
                ('service', models.CharField(max_length=100)),
                ('convenience_facilities', models.CharField(max_length=100)),
                ('satisfaction', models.CharField(max_length=100)),
                ('review_image', models.ImageField(blank=True, upload_to='review_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
