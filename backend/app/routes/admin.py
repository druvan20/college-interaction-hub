from flask import Blueprint, request, current_app as app
from app.utils import create_response

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/students', methods=['GET'])
def get_all_students():
    students = app.mongo.db.students.find()
    return create_response(data=list(students))

@admin_bp.route('/parents', methods=['GET'])
def get_all_parents():
    parents = app.mongo.db.parents.find()
    return create_response(data=list(parents))
