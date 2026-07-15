import requests
from config import API_KEY, BASE_URL


def get_current_weather(city, unit="metric"):
    """
    Fetch current weather for a city.
    """
    url = (
        f"{BASE_URL}weather?"
        f"q={city}&appid={API_KEY}&units={unit}"
    )

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            return {
                "error": data.get("message", "Unable to fetch weather.")
            }

    except requests.exceptions.ConnectionError:
        return {
            "error": "No internet connection."
        }

    except requests.exceptions.Timeout:
        return {
            "error": "Request timed out."
        }

    except requests.exceptions.RequestException:
        return {
            "error": "Something went wrong."
        }


def get_forecast(city, unit="metric"):
    """
    Fetch 5-day / 3-hour forecast.
    """
    url = (
        f"{BASE_URL}forecast?"
        f"q={city}&appid={API_KEY}&units={unit}"
    )

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            return {
                "error": data.get("message", "Unable to fetch forecast.")
            }

    except requests.exceptions.ConnectionError:
        return {
            "error": "No internet connection."
        }

    except requests.exceptions.Timeout:
        return {
            "error": "Request timed out."
        }

    except requests.exceptions.RequestException:
        return {
            "error": "Something went wrong."
        }