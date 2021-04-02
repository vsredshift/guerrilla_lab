from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    """ Main Blog Post class """
    title = models.CharField(max_length=100)
    content = models.TextField()
    sub_title = models.CharField(max_length=255, default=content)
    # auto_now=True -- original date lost on update  # auto_now_add -- keeps original
    date_posted = models.DateTimeField(default=timezone.now)
    # Delete posts of deleted users
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=30, default="untagged")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # redirects back to post detail page after submitting/updating post
        return reverse("post-detail", kwargs={"pk": self.pk})
        # If we want to go back to home page
        # return reverse("blog-home")
    

class Category(models.Model):
    category_name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
         return reverse("blog-home")
    
