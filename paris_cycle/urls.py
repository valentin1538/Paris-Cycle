from django import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core import views  # On importe les vues de ton app 'core'

urlpatterns = [
    # 1. L'administration Django
    path('admin/', admin.site.urls),

    # 2. Ta page d'accueil (le template avec la carte et les news)
    path('', views.index, name='index'),

    # 3. Les routes nécessaires pour la PWA (Service Worker, etc.)
    path('', include('pwa.urls')),
    
    # 4. L'API pour les stations Vélib'
    path("api/bikes/", include("core.urls")),
]

# 4. Configuration pour afficher les images des articles en développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)