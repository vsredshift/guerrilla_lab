from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    # create 1-to-1 relationship user/profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=1000)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    live_image = models.URLField(
        default='https://live.staticflickr.com/65535/50994357777_353292d837_n.jpg')

    def __str__(self):
        return f'{self.user.username} Profile'
