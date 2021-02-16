import pytest

from backend.app import create_app
import json


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('backend.config.DefaultConfig')

    testing_client = flask_app.test_client()

    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client  # this is where the testing happens!

    ctx.pop()


# Next 2 tests should always be on top of the file to avoid 5 minutes cache to keep data from other tests!
def test_get_cached_cities_with_empty_cache(test_client):
    response = test_client.get('api/v1/weather')
    assert json.loads(response.data) == []
    assert response.status_code == 200


def test_get_cached_cities(test_client):
    city_name = "Pindamonhangaba"

    response = test_client.get('api/v1/weather')
    assert json.loads(response.data) == []
    assert response.status_code == 200

    response = test_client.get(f'api/v1/weather/{city_name}')
    assert response.status_code == 200
    city_data = json.loads(response.data)

    response = test_client.get('api/v1/weather')
    assert response.status_code == 200

    cached_data = json.loads(response.data)
    assert cached_data == [city_data]


def test_get_city_weather(test_client):
    city_name = "Pindamonhangaba"
    response = test_client.get(f'api/v1/weather/{city_name}')

    assert response.status_code == 200

    data = json.loads(response.data)
    assert data.get('city') == city_name
    assert ('weather' and 'temperature') in data.keys()


def test_get_city_weather_with_invalid_city_name(test_client):
    city_name = "gfghjkj"
    response = test_client.get(f'api/v1/weather/{city_name}')

    assert response.status_code == 404

    data = json.loads(response.data)
    assert not data






