from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from .config import config_options
from .views import CachedCitiesWeatherView, CityWeatherView
from .extensions import cache, flask_bcrypt


def register_extensions(app):
    CORS(app, resources={r"*": {"origins": "*"}})
    cache.init_app(app)
    flask_bcrypt.init_app(app)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])

    register_extensions(app)

    api = Api(app)
    api.add_resource(CachedCitiesWeatherView, '/api/v1/weather')
    api.add_resource(CityWeatherView, '/api/v1/weather/<string:city_name>')

    return app



