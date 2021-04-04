from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    # create 1-to-1 relationship user/profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=1000, blank=True, null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    # social media links
    website = models.CharField(max_length=300, blank=True, null=True)
    linkedin = models.CharField(max_length=300, blank=True, null=True)
    github = models.CharField(max_length=300, blank=True, null=True)
    twitter = models.CharField(max_length=300, blank=True, null=True)
    instagram = models.CharField(max_length=300, blank=True, null=True)
    facebook = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        """ inherits args and kwargs of parent class.
            Used for handling files in local storage -
            not for deployment 
        """
        super().save(*args, **kwargs)

        # Override save method to handle large images
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)    # set max size
            img.thumbnail(output_size)  # resize image
            img.save(self.image.path)   # save scaled down image
