import os

from flask_script import Manager
from decouple import config as env

from app import create_app

app = create_app(env("ENVIRONMENT", default='dev'))

app.app_context().push()

manager = Manager(app)


@manager.command
def run():
    app.run()


@manager.command
def test():
    os.system("pytest")


@manager.option('-b', '--bind', dest='host', default='127.0.0.1')
@manager.option('-p', '--port', dest='port', type=int, default=6969)
@manager.option('-w', '--workers', dest='workers', type=int, default=3)
def gunicorn(host, port, workers):
    """Start the Server with Gunicorn"""
    from gunicorn.app.base import Application

    class FlaskApplication(Application):
        def init(self, parser, opts, args):
            return {
                'bind': f'{host}:{port}',
                'workers': workers
            }

        def load(self):
            return app

    application = FlaskApplication()
    return application.run()


if __name__ == '__main__':
    manager.run()
