from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name="home"),
    path('stlist/',views.stlist,name='stlist'),
    path('colist/',views.colist,name='colist'),
]
