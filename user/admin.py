from django.contrib import admin

# Register your models here.

from .models import UserSearchHistory, Profile

admin.site.register(UserSearchHistory)
admin.site.register(Profile)

