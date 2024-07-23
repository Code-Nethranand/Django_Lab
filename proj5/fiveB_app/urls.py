from django.urls import path
from .import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('5b/', views.stlist, name='stlist'),
    path('search', csrf_exempt(views.search), name='search'),
]
