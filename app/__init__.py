from flask import Flask, current_app, jsonify
from flask_migrate import Migrate
from .models import config_db
from .serializer import config_ma
from .blueprints.hello_world import hello_world_bp
from dotenv import load_dotenv
import os


def route_not_found(e):
    #change this method to your prefered way of handling errors
    return "can't resolve url", 404


def create_app():
    #flask application created on the factory method
    app = Flask(__name__)
    #setting SQLAlchemy database using the environment URI 
    load_dotenv()
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
    #configure the database and migrations
    config_db(app)
    config_ma(app)
    migrate = Migrate(app, app.db)
    #register all blueprints and errors routes
    app.register_blueprint(hello_world_bp)
    app.register_error_handler(404,route_not_found)
    return app

