from flask_restful import Resource, reqparse
from weather_manager import WeatherManager

parser = reqparse.RequestParser()
parser.add_argument("max", type=int, help="Max number of cities to retrieve from cache", required=False)


class CachedCitiesWeatherView(Resource):
    def get(self):
        weather_manager = WeatherManager('cache')
        max_number = parser.parse_args().get("max")
        weather_manager.get_cached_cities_weather(max_number)
        return {'response': 'teste'}


class CityWeatherView(Resource):
    def get(self, city_name: str):
        weather_manager = WeatherManager('cache', city_name)
        weather_manager.get_city_weather()
        return {'response': f'{city_name}'}
