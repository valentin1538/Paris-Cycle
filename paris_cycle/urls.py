"""
URL configuration for paris_cycle project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
]

# 4. Configuration pour afficher les images des articles en développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)