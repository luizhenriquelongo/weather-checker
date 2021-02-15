from flask import Flask
from flask_restful import Api

from backend.app.views import CachedCitiesWeatherView, CityWeatherView
from backend.extensions import cache


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_name)
    register_extensions(app)

    api = Api(app)
    api.add_resource(CachedCitiesWeatherView, '/weather')
    api.add_resource(CityWeatherView, '/weather/<string:city_name>')

    return app


def register_extensions(app):
    cache.init_app(app)
