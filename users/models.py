from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    # create 1-to-1 relationship user/profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=1000)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    

    def __str__(self):
        return f'{self.user.username} Profile'
