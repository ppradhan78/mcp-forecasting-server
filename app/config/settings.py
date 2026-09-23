import os

from dotenv import load_dotenv

load_dotenv()


class WeatherConfig:

    API_KEY = os.getenv("WEATHER_API_KEY")

    API_URL = os.getenv(
        "WEATHER_API_URL",
        "https://api.openweathermap.org/data/2.5/weather"
    )