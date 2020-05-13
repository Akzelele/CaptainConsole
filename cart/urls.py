from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="cart-index"),
    path('items', views.post_item_list, name="item-list"),
    path('checkout', views.checkout_view, name="checkout_view")
]
