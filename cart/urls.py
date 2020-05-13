from django.urls import path
from .views import (
    index,
    post_item_list,
    CheckoutView)

urlpatterns = [
    path('', index, name="cart-index"),
    path('items', post_item_list, name="item-list"),
    path('checkout/', CheckoutView.as_view(), name='checkout')
]
