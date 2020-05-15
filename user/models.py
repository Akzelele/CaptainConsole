from django.contrib.auth.decorators import login_required
from django.db import models
from django.contrib.auth.models import User
from item.models import Item
from datetime import datetime


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(default='Waluigi.png', blank=True, upload_to='profile_images')


class UserSearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    visited = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.item.name)

    class Meta:
        verbose_name_plural = "User search histories"


@login_required
def create_user_history(request):
    primary_item_key = int(request.path.split("/")[2])
    if not UserSearchHistory.objects.filter(user=request.user.id, item=Item.objects.get(pk=primary_item_key)).exists():
        # only assigns if user first time visiting website to avoid duplicates
        date = datetime.now()
        UserSearchHistory(
            user=request.user,
            item=Item.objects.get(pk=primary_item_key),
            visited=date).save()
