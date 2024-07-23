from django.urls import path
from .views import todaytime

urlpatterns = [
    path('',todaytime,name="todaytime"),
]