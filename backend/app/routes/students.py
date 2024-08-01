from flask import Blueprint, request, current_app as app
from app.models import Student
from app.utils import create_response

students_bp = Blueprint('students', __name__)

@students_bp.route('/', methods=['GET'])
def get_students():
    students = app.mongo.db.students.find()
    return create_response(data=[Student.from_mongo(student).to_mongo() for student in students])

@students_bp.route('/', methods=['POST'])
def add_student():
    data = request.json
    student = Student(None, data['name'], data['email'], data['enrollment_no'], data['department'], data['year'])
    app.mongo.db.students.insert_one(student.to_mongo())
    return create_response(message="Student added successfully")
