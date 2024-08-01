from flask import Blueprint, request, current_app as app
from app.models import Parent
from app.utils import create_response

parents_bp = Blueprint('parents', __name__)

@parents_bp.route('/', methods=['GET'])
def get_parents():
    parents = app.mongo.db.parents.find()
    return create_response(data=[Parent.from_mongo(parent).to_mongo() for parent in parents])

@parents_bp.route('/', methods=['POST'])
def add_parent():
    data = request.json
    parent = Parent(None, data['name'], data['email'], data['phone'], data['student_id'])
    app.mongo.db.parents.insert_one(parent.to_mongo())
    return create_response(message="Parent added successfully")
