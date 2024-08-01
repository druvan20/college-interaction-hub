# backend/app/models.py

from flask_pymongo import ObjectId

class Student:
    def __init__(self, _id, name, email, enrollment_no, department, year):
        self.id = str(_id) if _id else None
        self.name = name
        self.email = email
        self.enrollment_no = enrollment_no
        self.department = department
        self.year = year

    @staticmethod
    def from_mongo(data):
        return Student(
            data['_id'],
            data['name'],
            data['email'],
            data.get('enrollment_no', ''),
            data.get('department', ''),
            data.get('year', '')
        )

    def to_mongo(self):
        return {
            "_id": ObjectId(self.id) if self.id else None,
            "name": self.name,
            "email": self.email,
            "enrollment_no": self.enrollment_no,
            "department": self.department,
            "year": self.year
        }

class Placement:
    def __init__(self, _id, company, position, description, date):
        self.id = str(_id) if _id else None
        self.company = company
        self.position = position
        self.description = description
        self.date = date

    @staticmethod
    def from_mongo(data):
        return Placement(
            data['_id'],
            data['company'],
            data['position'],
            data['description'],
            data['date']
        )

    def to_mongo(self):
        return {
            "_id": ObjectId(self.id) if self.id else None,
            "company": self.company,
            "position": self.position,
            "description": self.description,
            "date": self.date
        }

class Parent:
    def __init__(self, _id, name, email, phone, student_id):
        self.id = str(_id) if _id else None
        self.name = name
        self.email = email
        self.phone = phone
        self.student_id = student_id

    @staticmethod
    def from_mongo(data):
        return Parent(
            data['_id'],
            data['name'],
            data['email'],
            data['phone'],
            data['student_id']
        )

    def to_mongo(self):
        return {
            "_id": ObjectId(self.id) if self.id else None,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "student_id": self.student_id
        }

class Event:
    def __init__(self, _id, name, description, date):
        self.id = str(_id) if _id else None
        self.name = name
        self.description = description
        self.date = date

    @staticmethod
    def from_mongo(data):
        return Event(
            data['_id'],
            data['name'],
            data['description'],
            data['date']
        )

    def to_mongo(self):
        return {
            "_id": ObjectId(self.id) if self.id else None,
            "name": self.name,
            "description": self.description,
            "date": self.date
        }
