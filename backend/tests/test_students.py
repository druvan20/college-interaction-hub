import unittest
from app import create_app
from app.models import Student

class StudentTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.config['MONGO_DBNAME'] = 'testdb'
        self.app.config['TESTING'] = True
        with self.app.app_context():
            self.db = self.app.mongo.db

    def tearDown(self):
        with self.app.app_context():
            self.db.students.delete_many({})

    def test_add_student(self):
        response = self.client.post('/students/', json={
            'name': 'John Doe',
            'email': 'john@example.com',
            'enrollment_no': '12345',
            'department': 'Computer Science',
            'year': 'Sophomore'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Student added successfully', response.json['message'])

    def test_get_students(self):
        self.client.post('/students/', json={
            'name': 'John Doe',
            'email': 'john@example.com',
            'enrollment_no': '12345',
            'department': 'Computer Science',
            'year': 'Sophomore'
        })
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json['data']), 1)

if __name__ == '__main__':
    unittest.main()
