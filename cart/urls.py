from django.urls import path
from .views import (
    index,
    post_item_list,
    checkout_view)

urlpatterns = [
    path('', index, name="cart-index"),
    path('items', post_item_list, name="item-list"),
    path('checkout', checkout_view, name="checkout_view")
]
