import requests

VELIB_API_URL = (
    "https://parisdata.opendatasoft.com/api/explore/v2.1/catalog/datasets/velib-disponibilite-en-temps-reel/records"
)

def get_velib_stations(limit=100, offset=0):
    """
    Récupère les stations Vélib' depuis l'API Paris Data.
    Retourne une liste de stations ou une liste vide en cas d'erreur.
    """
    params = {
        "limit": limit,
        "offset": offset,
    }

    try:
        response = requests.get(VELIB_API_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("results", [])
    except requests.exceptions.RequestException as e:
        print(f"Erreur API Vélib' : {e}")
        return []


def format_station(raw):
    """
    Nettoie et structure une station brute de l'API.
    """
    geo = raw.get("coordonnees_geo") or {}
    return {
        "stationcode": raw.get("stationcode"),
        "name": raw.get("name"),
        "is_installed": raw.get("is_installed"),
        "capacity": raw.get("capacity"),
        "numdocksavailable": raw.get("numdocksavailable"),
        "numbikesavailable": raw.get("numbikesavailable"),
        "mechanical": raw.get("mechanical"),
        "ebike": raw.get("ebike"),
        "is_renting": raw.get("is_renting"),
        "is_returning": raw.get("is_returning"),
        "duedate": raw.get("duedate"),
        "nom_arrondissement_communes": raw.get("nom_arrondissement_communes"),
        "code_insee_commune": raw.get("code_insee_commune"),
        "station_opening_hours": raw.get("station_opening_hours"),
        "coordonnees_geo": {
            "lon": geo.get("lon"),
            "lat": geo.get("lat"),
        },
    }


def get_formatted_stations(limit=100):
    raw_stations = get_velib_stations(limit=limit)
    return [format_station(s) for s in raw_stations]