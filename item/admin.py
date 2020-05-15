from django.contrib import admin

# Register your models here.
from .models import Item, ItemImage, ItemCategory

admin.site.register(Item)
admin.site.register(ItemImage)
admin.site.register(ItemCategory)
