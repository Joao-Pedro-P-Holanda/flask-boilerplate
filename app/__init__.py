from datetime import timedelta
from flask import Flask
from flask_migrate import Migrate
from flask_talisman import Talisman
from flask_seasurf import SeaSurf
from .models import config_db
from .serializer import config_ma
from .blueprints.hello_world import hello_world_bp
from dotenv import load_dotenv
import os


def route_not_found(e: Exception):
    # change this method to your prefered way of handling errors
    return "can't resolve url", 404


def create_app():
    # flask application created on the factory method
    app = Flask(__name__)
    # setting SQLAlchemy database using the environment URI
    load_dotenv()
    app.secret_key = os.getenv("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
    # configure the database and migrations
    config_db(app)
    migrate = Migrate(app, app.db)

    # serialization
    config_ma(app)
    # Security headers and middlewares
    _ = Talisman(app)
    _ = SeaSurf(app)

    # register all blueprints and errors routes
    app.register_blueprint(hello_world_bp)
    app.register_error_handler(404, route_not_found)

    return app
