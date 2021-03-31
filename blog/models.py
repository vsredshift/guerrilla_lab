from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    """ Main Blog Post class """
    title = models.CharField(max_length=100)
    content = models.TextField()
    # auto_now=True -- original date lost on update  # auto_now_add -- keeps original
    date_posted = models.DateTimeField(default=timezone.now)
    # Delete posts of deleted users
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
