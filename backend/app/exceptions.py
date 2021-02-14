class OpenWeatherAPIException(Exception):
    def __init__(self, message: str = "An error has occurred during API request"):
        self.message = message
        super(OpenWeatherAPIException, self).__init__(self.message)
