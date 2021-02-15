import pytest

from backend.app.open_weather_api import OpenWeatherAPI


@pytest.fixture
def api_instance():
    return OpenWeatherAPI()


def test_get_weather_by_city_name(api_instance):
    city_name = "Pindamonhangaba"
    weather_data, status_code = api_instance.get_weather_by_city_name(city_name)

    assert isinstance(weather_data, dict)
    assert weather_data.get("name") == city_name.capitalize()
    assert status_code == 200


def test_get_weather_by_city_name_with_invalid_city_name(api_instance):
    city_name = "asdfghjk"
    weather_data, status_code = api_instance.get_weather_by_city_name(city_name)

    assert weather_data.get("cod") == '404'
    assert status_code == 404


def test_parse_query_params(api_instance):
    query_params = api_instance._parse_query_params(q='teste')

    assert ('q=teste' and 'appid=' and 'units=') in query_params

