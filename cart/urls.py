from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    index,
    post_item_list,
    contact_view,
    payment_view, review_view)

urlpatterns = [
    path('', index, name="cart-index"),
    path('items', post_item_list, name="item-list"),
    path('contact', contact_view, name="contact_view"),
    path('payment', payment_view, name="payment_view"),
    path('review', review_view, name="review_view")
]
