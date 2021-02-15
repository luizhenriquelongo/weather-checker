from flask_caching import Cache

from backend.app.exceptions import OpenWeatherAPIException
from backend.app.open_weather_api import OpenWeatherAPI
from flask import current_app

STATUS_CODES = {
    'SUCCESS': 200,
    'NOT_FOUND': 404,
    'ERROR': 400,
}


def error_response(error_message: str, status_code: int) -> (dict, int):
    return {"error": error_message}, status_code


class WeatherManager:
    def __init__(self, api_instance: OpenWeatherAPI, cache_instance: Cache, city_name: str = None):
        self.__api = api_instance
        self.__cache = cache_instance
        self.city = city_name.capitalize() if city_name else None

    def get_cached_cities_weather(self, max_number: int) -> (dict, int):
        max_number = max_number or 5
        cached_cities = self.__cache.get("cached_cities") or {}
        if not cached_cities:
            return {}, STATUS_CODES['NOT_FOUND']

        cities = list(cached_cities)
        if len(cities) <= max_number:
            return cached_cities, STATUS_CODES['SUCCESS']

        cities = cities[:max_number]
        return {city: city_data for city, city_data in cached_cities.items() if city in cities}, STATUS_CODES['SUCCESS']

    def get_city_weather(self) -> (dict, int):
        city_weather, status_code = self._get_city_weather_from_cache()
        if not city_weather:
            city_weather, status_code = self._fetch_api_data()

        return city_weather, status_code

    def _fetch_api_data(self) -> (dict, int):
        try:
            api_data, status_code = self.__api.get_weather_by_city_name(self.city)

        except OpenWeatherAPIException as error:
            return error_response(error.message, STATUS_CODES['ERROR'])

        else:
            if status_code == 200:
                self._cache_fetched_data(api_data)
                return api_data, STATUS_CODES['SUCCESS']

            return {}, STATUS_CODES['NOT_FOUND']

    def _get_city_weather_from_cache(self) -> (dict, int):
        cached_cities = self.__cache.get("cached_cities") or {}
        if self.city and self.city in cached_cities.keys():
            return cached_cities[self.city], STATUS_CODES['SUCCESS']

        return {}, STATUS_CODES['NOT_FOUND']

    def _cache_fetched_data(self, data: dict) -> None:
        cached_cities = self.__cache.get("cached_cities") or {}
        cached_cities.update({data["name"]: data})
        self.__cache.set("cached_cities", cached_cities)
