from django.http import JsonResponse
from .services import get_formatted_stations

def stations_list(request):
    """
    Retourne toutes les stations Vélib' en JSON.
    Accepte un paramètre GET ?limit=XX
    """
    limit = int(request.GET.get("limit", 100))
    stations = get_formatted_stations(limit=limit)
    return JsonResponse({"count": len(stations), "stations": stations})