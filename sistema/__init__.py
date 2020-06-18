import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app(script_info=None):
    app = Flask(__name__)

    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    db.init_app(app)

    from sistema.api.ping import ping_blueprint
    from sistema.api.usuarios import usuarios_blueprint
    app.register_blueprint(ping_blueprint)
    app.register_blueprint(usuarios_blueprint)

    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app
