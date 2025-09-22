#config.py

import requests
from models import Weather

def geo(point, weather: Weather):
    geocoding_url = f"https://geocoding-api.open-meteo.com/v1/search?name={point.name}&count=10&language=en&format=json"
    response = requests.get(geocoding_url)
    data = response.json()

    lat = data["results"][0]["latitude"]
    lon = data["results"][0]["longitude"]

    param_map = {
        "temperature": "temperature_2m",
        "relative_Humidity": "relative_humidity_2m",
        "apparent_Temperature": "apparent_temperature",
        "is_Day_or_Night": "is_day",
        "precipitation": "precipitation",
        "rain": "rain",
        "showers": "showers",
        "snowfall": "snowfall",
        "weather_code": "weathercode",
        "cloud_cover_Total": "cloudcover",
        "sealevel_Pressure": "pressure_msl",
        "surface_Pressure": "surface_pressure",
        "wind_Speed": "windspeed_10m",
        "wind_Direction": "winddirection_10m",
        "wind_Gusts": "windgusts_10m",
    }

    variables = [
        param_map[p] for p, v in weather.model_dump().items() if v is True
    ]

    vars_str = ",".join(variables)
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current={vars_str}"
    weather_resp = requests.get(weather_url).json()

    return {"lat": lat, "lon": lon, "weather": weather_resp.get("current", {})}