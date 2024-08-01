from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
from .routes.students import students_bp
from .routes.parents import parents_bp
from .routes.admin import admin_bp
from .routes.placements import placements_bp
from .routes.events import events_bp
from dotenv import load_dotenv
import os
import logging
logging.basicConfig(level=logging.DEBUG)

# Load environment variables
load_dotenv()

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config.from_pyfile('config.py')
    mongo = PyMongo(app)
    
    app.mongo = mongo
    
    # Register blueprints
    app.register_blueprint(students_bp, url_prefix='/students')
    app.register_blueprint(parents_bp, url_prefix='/parents')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(placements_bp, url_prefix='/placements')
    app.register_blueprint(events_bp, url_prefix='/events')
    
    return app
