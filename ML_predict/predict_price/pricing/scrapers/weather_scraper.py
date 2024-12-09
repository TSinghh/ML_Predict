import requests

def fetch_weather_data(lat, lon):
    api_key ='015570c04c858f8109ef41bffd6c17d9'
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    
    response = requests.get(url).json()
    
    if response.get("main"):
        temp = response["main"]["temp"]
        rain = "rain" in response
        return {"temperature": temp, "rain": rain}
    else:
        return None
