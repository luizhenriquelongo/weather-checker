from flask_caching import Cache

from backend.app.exceptions import OpenWeatherAPIException
from backend.app.open_weather_api import OpenWeatherAPI
from backend.app.utils import StatusCode, error_response


class WeatherManager:
    """This class is used to manage all business logic behind views"""
    def __init__(self, api_instance: OpenWeatherAPI, cache_instance: Cache, city_name: str = None):
        self.__api = api_instance
        self.__cache = cache_instance
        self.city = city_name.capitalize() if city_name else None

    def get_cached_cities_weather(self, max_number: int) -> (dict, int):
        """Returns all cached cities up to max_number"""
        max_number = max_number or 5
        cached_cities = self.__cache.get('cached_cities') or {}
        if not cached_cities:
            return {}, StatusCode.NOT_FOUND

        cities = list(cached_cities)
        if len(cities) <= max_number:
            return cached_cities, StatusCode.SUCCESS

        cities = cities[:max_number]
        return {city: city_data for city, city_data in cached_cities.items() if city in cities}, StatusCode.SUCCESS

    def get_city_weather(self) -> (dict, int):
        """
            Returns a specific city weather,
            first tries to get it from cache and if there is no data,
            fetch the OpenWeatherAPI do get the weather data
        """
        city_weather, status_code = self._get_city_weather_from_cache()
        if not city_weather:
            city_weather, status_code = self._fetch_api_data()

        return {self.city: city_weather}, status_code

    def _fetch_api_data(self) -> (dict, int):
        """This is used to get a specific city weather data by using an API method"""
        try:
            api_data, status_code = self.__api.get_weather_by_city_name(self.city)

        except OpenWeatherAPIException as error:
            return error_response(error.message, StatusCode.ERROR)

        else:
            if status_code == 200:
                self._cache_fetched_data(api_data)
                return self._clean_data(api_data), StatusCode.SUCCESS

            return {}, StatusCode.NOT_FOUND

    def _get_city_weather_from_cache(self) -> (dict, int):
        """This is used to retrieve city weather data from cache"""
        cached_cities = self.__cache.get('cached_cities') or {}
        if self.city and self.city in cached_cities.keys():
            return cached_cities[self.city], StatusCode.SUCCESS

        return {}, StatusCode.NOT_FOUND

    def _cache_fetched_data(self, data: dict) -> None:
        """This is used to cache city weather data"""
        cached_cities = self.__cache.get('cached_cities') or {}

        city_data = self._clean_data(data)
        if city_data:
            cached_cities.update({self.city: city_data})
            self.__cache.set('cached_cities', cached_cities)

    def _clean_data(self, data: dict) -> dict or None:
        """This is used to clean data to return useful information"""
        try:
            weather_condition = data['weather'][0]['main']
        except (IndexError, KeyError):
            weather_condition = None

        temperature = data.get('main', {}).get('temp')

        if weather_condition and temperature:
            return {
                "weather": weather_condition,
                "temperature": f'{int(round(temperature))}ºC'
            }
