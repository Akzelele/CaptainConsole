from django.contrib import admin

# Register your models here.
from .models import Console, Manufacturer, ConsoleImage

admin.site.register(Console)
admin.site.register(Manufacturer)
admin.site.register(ConsoleImage)