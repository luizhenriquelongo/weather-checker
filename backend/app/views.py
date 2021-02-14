from flask_restful import Resource, reqparse

from .open_weather_api import OpenWeatherAPI
from .weather_manager import WeatherManager

parser = reqparse.RequestParser()
parser.add_argument("max", type=int, help="Max number of cities to retrieve from cache", required=False)

api = OpenWeatherAPI()


class CachedCitiesWeatherView(Resource):
    def get(self):
        from . import cache

        weather_manager = WeatherManager(api, cache)
        max_number = parser.parse_args().get("max")
        return weather_manager.get_cached_cities_weather(max_number)


class CityWeatherView(Resource):
    def get(self, city_name: str):
        from . import cache

        weather_manager = WeatherManager(api, cache, city_name)
        return weather_manager.get_city_weather()
