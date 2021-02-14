from flask_caching import Cache

from .exceptions import OpenWeatherAPIException
from .open_weather_api import OpenWeatherAPI


def error_response(error_message: str, status_code: int) -> (dict, int):
    return {"error": error_message}, status_code


class WeatherManager:
    def __init__(self, api_instance: OpenWeatherAPI, cache_instance: Cache, city_name: str = None):
        self.__api = api_instance
        self.__cache = cache_instance
        self.city = city_name.capitalize() if city_name else None

    def get_cached_cities_weather(self, max_number: int) -> dict:
        max_number = max_number or 5
        cached_cities = self.__cache.get("cached_cities") or {}
        cities = list(cached_cities)
        if len(cities) <= max_number:
            return cached_cities

        cities = cities[:max_number]
        return {city: city_data for city, city_data in cached_cities.items() if city in cities}

    def get_city_weather(self) -> dict:
        city_weather = self._get_city_weather_from_cache()
        if not city_weather:
            city_weather = self._fetch_api_data()

        return city_weather

    def _fetch_api_data(self) -> dict:
        try:
            api_data = self.__api.get_weather_by_city_name(self.city)

        except OpenWeatherAPIException as error:
            error_response(error.message, 400)

        else:
            self._cache_fetched_data(api_data)
            return api_data

    def _get_city_weather_from_cache(self) -> dict:
        cached_cities = self.__cache.get("cached_cities") or {}
        if self.city and self.city in cached_cities.keys():
            return cached_cities[self.city]

    def _cache_fetched_data(self, data: dict) -> None:
        cached_cities = self.__cache.get("cached_cities") or {}
        cached_cities.update({data["name"]: data})
        self.__cache.set("cached_cities", cached_cities)
