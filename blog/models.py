from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from django.utils.text import slugify
from django.urls import reverse
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager


class Post(models.Model):
    """ Main Blog Post class """
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, null=False,
                            unique=True, default=title)
    # slug = AutoSlugField(populate_from='title',
    #                      default='old_post')
    content = RichTextField(blank=True, null=True)      # Rich text editor
    subheading = models.TextField(max_length=350, blank=True, default=None)
    date_posted = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=30, default=None)
    head_image = models.ImageField(
        blank=True, null=True, upload_to='images/')
    tags = TaggableManager(blank=True)
    likes = models.ManyToManyField(User, related_name='blog_likes')
    dislikes = models.ManyToManyField(User, related_name='blog_dislikes')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # redirects back to post detail page after submitting/updating post
        return reverse("post-detail", kwargs={"pk": self.pk, "slug": self.slug})
        # If we want to go back to home page
        # return reverse("blog-home")

    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()


class Category(models.Model):
    category_name = models.CharField(max_length=30, primary_key=True)

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse("blog-home")

    class Meta:
        verbose_name_plural = "Categories"


class Comment(models.Model):
    comment = models.ForeignKey(
        Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.comment.title}, {self.name}'
