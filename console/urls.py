from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.get_console_by_id, name="console-index"),
]
