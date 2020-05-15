from django.db import models
from django.contrib.auth.models import User
from item.models import Item


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(default='Waluigi.png',blank=True, upload_to='profile_images')


class UserSearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    visited = models.DateField(auto_now=True)
