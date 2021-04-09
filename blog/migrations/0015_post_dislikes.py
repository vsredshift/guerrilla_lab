# Generated by Django 3.1.7 on 2021-04-04 17:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0014_auto_20210404_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dislikes',
            field=models.ManyToManyField(related_name='blog_dislikes', to=settings.AUTH_USER_MODEL),
        ),
    ]