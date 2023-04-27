# Generated by Django 3.2.18 on 2023-04-27 05:45

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
                ('country', models.TextField()),
                ('city', models.CharField(max_length=80)),
                ('price', models.IntegerField()),
                ('address', models.CharField(max_length=80)),
                ('post_image', models.ImageField(blank=True, upload_to='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('accuracy', models.IntegerField()),
                ('communication', models.IntegerField()),
                ('cleaniness', models.IntegerField()),
                ('location', models.IntegerField()),
                ('check_in', models.IntegerField()),
                ('value', models.IntegerField()),
                ('review_image', models.IntegerField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
