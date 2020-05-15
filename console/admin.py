from django.contrib import admin

# Register your models here.
from .models import Console, Manufacturer

admin.site.register(Console)
admin.site.register(Manufacturer)
