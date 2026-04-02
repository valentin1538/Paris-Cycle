from django.http import JsonResponse
from .services import get_formatted_stations
from django.shortcuts import render
from .models import Article
import json

def stations_list(request):
    """
    Retourne toutes les stations Vélib' en JSON.
    Accepte un paramètre GET ?limit=XX
    """
    limit = int(request.GET.get("limit", 100))
    stations = get_formatted_stations(limit=limit)
    return JsonResponse({"count": len(stations), "stations": stations})

# def index(request):
#     # On récupère les 3 dernières actualités
#     articles = Article.objects.all().order_by('-date_publication')[:3]
#     return render(request, 'core/index.html', {'articles': articles})

def index(request):
    articles = Article.objects.all().order_by('-date_publication')[:3]
    stations = get_formatted_stations(limit=100)
    return render(request, 'core/index.html', {
        'articles': articles,
        'stations_json': json.dumps(stations),  # on passe les stations au template
    })
