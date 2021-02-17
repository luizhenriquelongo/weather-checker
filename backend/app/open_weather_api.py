import urllib.parse

import requests
from requests import RequestException

from .exceptions import OpenWeatherAPIException
from .config import DefaultConfig


class OpenWeatherAPI:
    """This class contains all the requests logic to OpenWeatherAPI"""

    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    DEFAULT_QUERY_PARAMS = {
        "appid": DefaultConfig.OPEN_WEATHER_API_KEY,
        "units": "metric",
    }

    def get_weather_by_city_name(self, city_name: str) -> (dict, int):
        """This is used to make a GET request to OpenWeatherAPI to retrieve weather information about a city"""
        query_params = self._parse_query_params(q=city_name)

        try:
            response = requests.get(f'{self.BASE_URL}?{query_params}')

        except RequestException:
            raise OpenWeatherAPIException()

        return response.json(), response.status_code

    def _parse_query_params(self, **query_params):
        """This is used to encode query params"""
        query_params.update(self.DEFAULT_QUERY_PARAMS)
        return urllib.parse.urlencode(query_params)
