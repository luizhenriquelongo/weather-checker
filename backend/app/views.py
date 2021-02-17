from flask_restful import Resource, reqparse

from flask import current_app

from .open_weather_api import OpenWeatherAPI
from .weather_manager import WeatherManager

parser = reqparse.RequestParser()
parser.add_argument("max", type=int, help="Max number of cities to retrieve from cache", required=False)

api = OpenWeatherAPI()


class CachedCitiesWeatherView(Resource):
    def get(self):
        from .extensions import cache

        weather_manager = WeatherManager(api, cache)
        max_number = parser.parse_args().get("max") or current_app.config["MAX_CITIES_TO_RETRIEVE"]
        weather_data, status_code = weather_manager.get_cached_cities_weather(max_number)
        return weather_data, status_code


class CityWeatherView(Resource):
    def get(self, city_name: str):
        from .extensions import cache

        weather_manager = WeatherManager(api, cache, city_name)
        weather_data, status_code = weather_manager.get_city_weather()
        return weather_data, status_code
