from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('fiveA_app.urls')),
    path('',include('fiveB_app.urls')),
]
