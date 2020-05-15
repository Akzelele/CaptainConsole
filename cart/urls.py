from django.urls import path
from .views import (
    index,
    post_item_list,
    contact_view,
    payment_view,
    review_view,
    order_review)

urlpatterns = [
    path('', index, name="cart-index"),
    path('items', post_item_list, name="item-list"),
    path('contact', contact_view, name="contact_view"),
    path('payment', payment_view, name="payment_view"),
    path('review', review_view, name="review_view"),
    path('order-review', order_review, name="order_review")
]
