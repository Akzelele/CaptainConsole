from django.db import models
from console.models import Console


# Create your models here.

class ItemCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999)
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    price = models.FloatField()
    on_sale = models.BooleanField()
    console = models.ForeignKey(Console, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ItemImage(models.Model):
    image = models.CharField(max_length=999)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.image)
