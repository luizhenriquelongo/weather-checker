class WeatherManager:
    def __init__(self, cache_instance, city_name: str = None):
        self.__cache = cache_instance
        if city_name:
            self.city = city_name

    def get_cached_cities_weather(self, max_number):
        pass

    def get_city_weather(self):
        pass

    def _get_city_weather_from_cache(self):
        pass

    def _fetch_api_data(self):
        pass

    def _cache_fetched_data(self, data: dict):
        pass
