import pytest

from backend.app.weather_manager import WeatherManager



@pytest.fixture
def cached_cities():
    return {
        "Pindamonhangaba": {
            "weather": "Clouds",
            "temperature": "22ºC"
        },
        "Taubaté": {
            "weather": "Clouds",
            "temperature": "22ºC"
        },
        "Tremembé": {
            "weather": "Clouds",
            "temperature": "22ºC"
        },
        "Caçapava": {
            "weather": "Clouds",
            "temperature": "22ºC"
        },
        "São José dos Campos": {
            "weather": "Clouds",
            "temperature": "22ºC"
        },
        "Jacareí": {
            "weather": "Clouds",
            "temperature": "22ºC"
        },
    }


def test_get_cached_cities_weather_with_empty_cache(mocker):
    cache = mocker.Mock()
    cache.get.return_value = None

    wm = WeatherManager(api_instance=mocker.Mock(), cache_instance=cache)
    weather_data, status_code = wm.get_cached_cities_weather(max_number=None)

    cache.get.assert_called_with('cached_cities')

    assert weather_data == {}
    assert status_code == 404


def test_get_cached_cities_weather_with_default_max_number(mocker, cached_cities):
    cache = mocker.Mock()
    cache.get.return_value = cached_cities

    wm = WeatherManager(api_instance=mocker.Mock(), cache_instance=cache)
    weather_data, status_code = wm.get_cached_cities_weather(max_number=None)

    cache.get.assert_called_with('cached_cities')

    assert len(cached_cities) == 6
    assert len(weather_data.keys()) == 5
    assert status_code == 200


def test_get_cached_cities_weather_with_max_number(mocker, cached_cities):
    cache = mocker.Mock()
    cache.get.return_value = cached_cities

    wm = WeatherManager(api_instance=mocker.Mock(), cache_instance=cache)
    weather_data, status_code = wm.get_cached_cities_weather(max_number=3)

    cache.get.assert_called_with('cached_cities')

    assert len(cached_cities) == 6
    assert len(weather_data.keys()) == 3
    assert status_code == 200


def test_get_city_weather_with_empty_cache(mocker):
    city_name = "Pindamonhangaba"
    mocked_return = ({city_name: {}}, 200)
    mocked_get_city_weather_from_cache = mocker.patch(
        "backend.app.weather_manager.WeatherManager._get_city_weather_from_cache"
    )
    mocked_get_city_weather_from_cache.return_value = (None, 404)

    mocked_fetch_api_data = mocker.patch(
        "backend.app.weather_manager.WeatherManager._fetch_api_data"
    )
    mocked_fetch_api_data.return_value = mocked_return

    wm = WeatherManager(api_instance=mocker.Mock(), cache_instance=mocker.Mock(), city_name=city_name)
    weather_data, status_code = wm.get_city_weather()

    mocked_get_city_weather_from_cache.assert_called_once()
    mocked_fetch_api_data.assert_called_once()

    assert weather_data, status_code == mocked_return


def test_get_city_weather_with_cached_data(mocker):
    city_name = "Pindamonhangaba"
    mocked_return = ({city_name: {}}, 200)
    mocked_get_city_weather_from_cache = mocker.patch(
        "backend.app.weather_manager.WeatherManager._get_city_weather_from_cache"
    )
    mocked_get_city_weather_from_cache.return_value = mocked_return

    mocked_fetch_api_data = mocker.patch(
        "backend.app.weather_manager.WeatherManager._fetch_api_data"
    )

    wm = WeatherManager(api_instance=mocker.Mock(), cache_instance=mocker.Mock(), city_name=city_name)
    weather_data, status_code = wm.get_city_weather()

    mocked_get_city_weather_from_cache.assert_called_once()
    mocked_fetch_api_data.assert_not_called()

    assert weather_data, status_code == mocked_return


def test_fetch_api_data(mocker):
    city_name = "Pindamonhangaba"
    mocked_return = ({}, 200)
    api = mocker.Mock()
    api.get_weather_by_city_name.return_value = mocked_return

    mocked_cache_fetch_data = mocker.patch(
        "backend.app.weather_manager.WeatherManager._cache_fetched_data"
    )
    mocked_clean_data = mocker.patch(
        "backend.app.weather_manager.WeatherManager._clean_data"
    )
    mocked_clean_data.return_value = mocked_return

    wm = WeatherManager(api_instance=api, cache_instance=mocker.Mock(), city_name=city_name)
    weather_data, status_code = wm._fetch_api_data()

    api.get_weather_by_city_name.assert_called_with(city_name)
    mocked_cache_fetch_data.assert_called_with(mocked_return[0])
    mocked_clean_data.assert_called_with(mocked_return[0])

    assert weather_data, status_code == mocked_return


def test_fetch_api_data_when_api_returns_404(mocker):
    city_name = "Pindamonhangaba"
    api = mocker.Mock()
    api.get_weather_by_city_name.return_value = ({'cod': '404'}, 404)

    mocked_cache_fetch_data = mocker.patch(
        "backend.app.weather_manager.WeatherManager._cache_fetched_data"
    )
    mocked_clean_data = mocker.patch(
        "backend.app.weather_manager.WeatherManager._clean_data"
    )

    wm = WeatherManager(api_instance=api, cache_instance=mocker.Mock(), city_name=city_name)
    weather_data, status_code = wm._fetch_api_data()

    api.get_weather_by_city_name.assert_called_with(city_name)
    mocked_cache_fetch_data.assert_not_called()
    mocked_clean_data.assert_not_called()

    assert weather_data == {}
    assert status_code == 404


def test_get_city_weather_from_cache(mocker, cached_cities):
    city_name = "Pindamonhangaba"

    cache = mocker.Mock()
    cache.get.return_value = cached_cities

    wm = WeatherManager(api_instance=mocker.Mock(), cache_instance=cache, city_name=city_name)
    weather_data, status_code = wm._get_city_weather_from_cache()

    cache.get.assert_called_with('cached_cities')

    assert weather_data == cached_cities[city_name]
    assert status_code == 200


def test_get_city_weather_from_cache_with_empty_cache(mocker):
    city_name = "Pindamonhangaba"

    cache = mocker.Mock()
    cache.get.return_value = None

    wm = WeatherManager(api_instance=mocker.Mock(), cache_instance=cache, city_name=city_name)
    weather_data, status_code = wm._get_city_weather_from_cache()

    cache.get.assert_called_with('cached_cities')

    assert weather_data == {}
    assert status_code == 404


def test_cache_fetched_data(mocker):
    city_name = "Pindamonhangaba"

    cache = mocker.Mock()
    cache.get.return_value = None

    mocked_data = {'weather': 'buddy'}
    mocked_clean_data = mocker.patch(
        "backend.app.weather_manager.WeatherManager._clean_data"
    )
    mocked_clean_data.return_value = mocked_data

    wm = WeatherManager(api_instance=mocker.Mock(), cache_instance=cache, city_name=city_name)
    wm._cache_fetched_data(mocked_data)

    cache.get.assert_called_with('cached_cities')
    mocked_clean_data.assert_called_with(mocked_data)
    cache.set.assert_called_with('cached_cities', {city_name: mocked_data})


def test_cache_fetched_data_with_invalid_data(mocker):
    city_name = "Pindamonhangaba"

    cache = mocker.Mock()
    cache.get.return_value = None

    mocked_data = {'weather': 'buddy'}
    mocked_clean_data = mocker.patch(
        "backend.app.weather_manager.WeatherManager._clean_data"
    )
    mocked_clean_data.return_value = None

    wm = WeatherManager(api_instance=mocker.Mock(), cache_instance=cache, city_name=city_name)
    wm._cache_fetched_data(mocked_data)

    cache.get.assert_called_with('cached_cities')
    mocked_clean_data.assert_called_with(mocked_data)
    cache.set.assert_not_called()


def test_clean_data(mocker):
    data = {'weather': [{'main': 'Sunny'}], 'main': {'temp': 20}}
    city_name = "Pindamonhangaba"

    wm = WeatherManager(api_instance=mocker.Mock(), cache_instance=mocker.Mock(), city_name=city_name)
    cleaned_data = wm._clean_data(data)

    assert cleaned_data == {
        'weather': 'Sunny',
        'temperature': '20ºC'
    }


def test_clean_data_with_invalid_weather(mocker):
    data = {'weather': [], 'main': {'temp': 20}}
    city_name = "Pindamonhangaba"

    wm = WeatherManager(api_instance=mocker.Mock(), cache_instance=mocker.Mock(), city_name=city_name)
    cleaned_data = wm._clean_data(data)

    assert not cleaned_data


def test_clean_data_with_no_temperature(mocker):
    data = {'weather': [{'main': 'Sunny'}], 'main': {'another_prop': 20}}
    city_name = "Pindamonhangaba"

    wm = WeatherManager(api_instance=mocker.Mock(), cache_instance=mocker.Mock(), city_name=city_name)
    cleaned_data = wm._clean_data(data)

    assert not cleaned_data
