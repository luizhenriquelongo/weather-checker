from decouple import config as env


class DefaultConfig:
    SECRET_KEY = env("SECRET_KEY")
    OPEN_WEATHER_API_KEY = env("OPEN_WEATHER_API_KEY")
    CACHE_TYPE = "simple"
    CACHE_DEFAULT_TIMEOUT = env("CACHE_DEFAULT_TIMEOUT", default=300, cast=int)
    MAX_CITIES_TO_RETRIEVE = env("MAX_CITIES_TO_RETRIEVE", default=5, cast=int)


class DevelopmentConfig(DefaultConfig):
    DEBUG = True


class TestingConfig(DefaultConfig):
    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(DefaultConfig):
    DEBUG = False


config_options = {
    "dev": DevelopmentConfig,
    "test": TestingConfig,
    "prod": ProductionConfig,
}

key = DefaultConfig.SECRET_KEY
