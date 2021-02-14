import os
import urllib.parse

import requests
from requests import RequestException

from .exceptions import OpenWeatherAPIException


class OpenWeatherAPI:
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    DEFAULT_QUERY_PARAMS = {
        "appid": os.getenv("OPEN_WEATHER_API_KEY"),
        "units": "metric",
    }

    def get_weather_by_city_name(self, city_name: str) -> dict:
        query_params = self._parse_query_params(q=city_name)

        try:
            response = requests.get(f'{self.BASE_URL}?{query_params}')

        except RequestException:
            raise OpenWeatherAPIException()

        return response.json()

    def _parse_query_params(self, **query_params):
        query_params.update(self.DEFAULT_QUERY_PARAMS)
        return urllib.parse.urlencode(query_params)


if __name__ == '__main__':
    api = OpenWeatherAPI()
    print(api.get_weather_by_city_name('asjdhkajsd'))
