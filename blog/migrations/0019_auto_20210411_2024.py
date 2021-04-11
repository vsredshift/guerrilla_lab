# Generated by Django 3.1.7 on 2021-04-11 18:24

from django.db import migrations, models
from blog.utils import unique_slug_generator


def update_slug(apps, schema_editor):
    Post = apps.get_model('blog', 'Post')

    for instance in Post.objects.all():
        if not instance.slug:
            instance.slug = unique_slug_generator(
                instance, instance.title, instance.slug)
            instance.save()


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20210411_2015'),
    ]

    operations = [
        migrations.RunPython(
            update_slug, reverse_code=migrations.RunPython.noop),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
