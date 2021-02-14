from flask import Flask
from flask_restful import Api

from app.views import CachedCitiesWeatherView, CityWeatherView

app = Flask(__name__)
api = Api(app)
api.add_resource(CachedCitiesWeatherView, '/weather')
api.add_resource(CityWeatherView, '/weather/<string:city_name>')

if __name__ == '__main__':
    app.run()
