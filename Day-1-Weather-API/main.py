import requests

def get_weather(city):
    # Using Open-Meteo’s free API
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city}

    try:
        # Step 1: Get coordinates for the city
        geo_response = requests.get(url, params=params)
        geo_response.raise_for_status()
        geo_data = geo_response.json()

        if "results" not in geo_data or not geo_data["results"]:
            print("City not found.")
            return

        lat = geo_data["results"][0]["latitude"]
        lon = geo_data["results"][0]["longitude"]

        # Step 2: Fetch weather data
        weather_url = "https://api.open-meteo.com/v1/forecast"
        weather_params = {
            "latitude": lat,
            "longitude": lon,
            "current_weather": True
        }

        weather_response = requests.get(weather_url, params=weather_params)
        weather_response.raise_for_status()
        weather_data = weather_response.json()

        current = weather_data["current_weather"]
        print(f"\n🌤 Weather in {city}:")
        print(f"Temperature: {current['temperature']}°C")
        print(f"Windspeed: {current['windspeed']} km/h")
        print(f"Time: {current['time']}")
        
    except requests.exceptions.RequestException as e:
        print("Error fetching weather data:", e)

city=input("Enter the city you want to check weather: ")
get_weather(city)
