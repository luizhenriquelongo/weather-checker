from flask_caching import Cache

from backend.app import create_app

app = create_app("config.DefaultConfig")

if __name__ == '__main__':
    app.run()
