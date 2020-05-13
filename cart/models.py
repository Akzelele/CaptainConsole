from django.db import models
from django import forms
from item.models import Item
from django_countries.fields import CountryField


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


class Order(models.Model):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField()
    country = CountryField().formfield()
    street_name = forms.CharField(max_length=255)
    house_number = forms.IntegerField(min_value=0, max_value=100000)
    city = forms.CharField(max_length=255)
    zip = forms.CharField(max_length=10)
    items = models.ManyToManyField(OrderItem)
