# Generated by Django 5.1.1 on 2024-09-23 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_merge_20240923_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recentwork',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
