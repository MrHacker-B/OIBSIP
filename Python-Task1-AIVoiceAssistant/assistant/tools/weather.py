import requests
from assistant.config import WEATHER_API_KEY

API_KEY = WEATHER_API_KEY

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        return "Sorry, I couldn't find that city."

    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"]

    return f"The temperature in {city} is {temperature} degrees Celsius with {description}."