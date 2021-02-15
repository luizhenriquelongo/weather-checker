class StatusCode:
    """Helper class to hold status codes"""
    SUCCESS = 200
    NOT_FOUND = 404
    ERROR = 400


def error_response(error_message: str, status_code: int) -> (dict, int):
    return {'error': error_message}, status_code
