from django import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pwa.urls')), # <--- INDISPENSABLE pour le Service Worker
    path("api/bikes/", include("core.urls")),
]
