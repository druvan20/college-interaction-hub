from flask import Blueprint, request, current_app as app
from app.models import Event
from app.utils import create_response

events_bp = Blueprint('events', __name__)

@events_bp.route('/', methods=['GET'])
def get_events():
    events = app.mongo.db.events.find()
    return create_response(data=[Event.from_mongo(event).to_mongo() for event in events])

@events_bp.route('/', methods=['POST'])
def add_event():
    data = request.json
    event = Event(None, data['name'], data['description'], data['date'])
    app.mongo.db.events.insert_one(event.to_mongo())
    return create_response(message="Event added successfully")
