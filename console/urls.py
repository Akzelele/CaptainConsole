from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.index, name="console-index"),
    path('<int:id>', views.manufacturer_index, name='manufacturer-index')
]
