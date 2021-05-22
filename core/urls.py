from django.urls import path
from .views import UUIDView

urlpatterns = [
    path('',UUIDView.as_view())
]