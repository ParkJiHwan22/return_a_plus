# Generated by Django 3.2.18 on 2023-05-03 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20230503_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='accessibility',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='review',
            name='convenience_facilities',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='review',
            name='cost',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='review',
            name='service',
            field=models.CharField(max_length=100),
        ),
    ]
