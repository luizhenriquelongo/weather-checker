from decouple import config as env


class DefaultConfig:
    DEBUG = env("DEBUG", default=False, cast=bool)
    OPEN_WEATHER_API_KEY = env("OPEN_WEATHER_API_KEY")
    CACHE_TYPE = "simple"
    CACHE_DEFAULT_TIMEOUT = env("CACHE_DEFAULT_TIMEOUT", default=320, cast=int)
    ENV = env("ENV", default="production")
    SECRET_KEY = env("SECRET_KEY")
    MAX_CITIES_TO_RETRIEVE = env("MAX_CITIES_TO_RETRIEVE", default=5, cast=int)
