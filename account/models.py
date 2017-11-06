from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import os
from PIL import Image

class UserProfile(models.Model):
    user =      models.OneToOneField(User, related_name = 'user')
    photo =     models.ImageField(upload_to='profile_images', null=True, blank=True)
    bio =       models.TextField(default='', blank=True)
    gender =    models.TextField(default='', blank=True)
    country =   models.CharField(max_length=100, default='', blank=True)

def __unicode__(self):
    return self.user.username
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

    post_save.connect(create_user_profile, sender=User)


