from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('threeA_app.urls')),
    path('',include('threeB_app.urls')),
]
