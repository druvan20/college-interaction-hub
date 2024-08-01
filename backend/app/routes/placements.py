from flask import Blueprint, request, current_app as app
from app.models import Placement
from app.utils import create_response

placements_bp = Blueprint('placements', __name__)

@placements_bp.route('/', methods=['GET'])
def get_placements():
    placements = app.mongo.db.placements.find()
    return create_response(data=[Placement.from_mongo(placement).to_mongo() for placement in placements])

@placements_bp.route('/', methods=['POST'])
def add_placement():
    data = request.json
    placement = Placement(None, data['company'], data['position'], data['description'], data['date'])
    app.mongo.db.placements.insert_one(placement.to_mongo())
    return create_response(message="Placement added successfully")
