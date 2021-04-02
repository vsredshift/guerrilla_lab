# Creating, updating and saving user profiles
# signal fired after object saved [we want to save after user creation]
from django.db.models.signals import post_save  
from django.contrib.auth.models import User     # Sender
from django.dispatch import receiver            # Receiver
from .models import Profile


""" When user is saved, send post_save signal. Receiver runs create_profile function """
@receiver(post_save, sender=User)   
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


""" Save profile when changes made """
@receiver(post_save, sender=User)   
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
