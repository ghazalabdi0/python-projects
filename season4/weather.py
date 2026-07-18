from fastapi import FastAPI, HTTPException, Query
import httpx

app = FastAPI(title="Weather API")

# API Key خود را اینجا قرار دهید
OPENWEATHER_API_KEY = "YOUR_API_KEY"


async def get_openmeteo_weather(lat: float, lon: float):
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}"
        f"&longitude={lon}"
        f"&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
    )

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="OpenMeteo API Error")

    data = response.json()["current"]

    return {
        "provider": "openmeteo",
        "temperature": data["temperature_2m"],
        "humidity": data["relative_humidity_2m"],
        "wind_speed": data["wind_speed_10m"]
    }


async def get_openweather_weather(lat: float, lon: float):
    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?lat={lat}"
        f"&lon={lon}"
        f"&appid={OPENWEATHER_API_KEY}"
        "&units=metric"
    )

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="OpenWeather API Error")

    data = response.json()

    return {
        "provider": "openweather",
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"]
    }


@app.get("/weather")
async def get_weather(
    lat: float = Query(..., ge=-90, le=90),
    lon: float = Query(..., ge=-180, le=180),
    provider: str = Query(...)
):

    if provider == "openmeteo":
        return await get_openmeteo_weather(lat, lon)

    elif provider == "openweather":
        return await get_openweather_weather(lat, lon)

    raise HTTPException(
        status_code=400,
        detail="Invalid provider. Use 'openweather' or 'openmeteo'."
    )