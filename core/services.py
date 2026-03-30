import requests

VELIB_API_URL = (
    "https://parisdata.opendatasoft.com/api/explore/v2.1/catalog/datasets/velib-disponibilite-en-temps-reel/records"
)

# Fallback in memory: if API is temporarily blocked (403/rate limit),
# keep displaying the most recent valid station payload.
_LAST_SUCCESSFUL_STATIONS = []

def get_velib_stations(limit=100, offset=0):
    global _LAST_SUCCESSFUL_STATIONS

    # Opendatasoft rejects large limits on this dataset (400).
    safe_limit = max(1, min(int(limit), 100))
    safe_offset = max(0, int(offset))

    params = {
        "limit": safe_limit,
        "offset": safe_offset,
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36",
        "Accept": "application/json",
    }

    try:
        response = requests.get(
            VELIB_API_URL,
            params=params,
            headers=headers,
            timeout=10
        )

        response.raise_for_status()
        data = response.json()
        results = data.get("results", [])
        if results:
            _LAST_SUCCESSFUL_STATIONS = results
        return results

    except requests.exceptions.RequestException as e:
        print(f"Erreur API Vélib' : {e}")
        if _LAST_SUCCESSFUL_STATIONS:
            print("Utilisation du dernier jeu de donnees Vélib' en cache.")
            return _LAST_SUCCESSFUL_STATIONS
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