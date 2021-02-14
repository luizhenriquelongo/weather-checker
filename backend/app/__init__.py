from flask import Flask
from flask_restful import Api
from flask_caching import Cache

from .views import CachedCitiesWeatherView, CityWeatherView

config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "simple", # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 10
}

app = Flask(__name__)
app.config.from_mapping(config)
cache = Cache(app)
api = Api(app)
api.add_resource(CachedCitiesWeatherView, '/weather')
api.add_resource(CityWeatherView, '/weather/<string:city_name>')
