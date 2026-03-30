from django.http import JsonResponse
from .services import get_formatted_stations
from django.shortcuts import render
from .models import Article

def stations_list(request):
    """
    Retourne toutes les stations Vélib' en JSON.
    Accepte un paramètre GET ?limit=XX
    """
    limit = int(request.GET.get("limit", 100))
    stations = get_formatted_stations(limit=limit)
    return JsonResponse({"count": len(stations), "stations": stations})

def index(request):
    # On récupère les 3 dernières actualités
    articles = Article.objects.all().order_by('-date_publication')[:3]
    return render(request, 'core/index.html', {'articles': articles})
