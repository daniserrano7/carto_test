from flask import Flask
from .routes import accumulated


# App factory
def create_app():
    app = Flask(__name__)

    # Route registering
    app.register_blueprint(accumulated.bp)

    return app
