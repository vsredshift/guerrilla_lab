# Generated by Django 3.1.7 on 2021-04-04 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_post_dislikes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='head_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
