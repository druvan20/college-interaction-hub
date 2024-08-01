import unittest
from app import create_app

class AdminTestCase(unittest.TestCase):
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
            self.db.parents.delete_many({})

    def test_get_all_students(self):
        self.client.post('/students/', json={
            'name': 'John Doe',
            'email': 'john@example.com',
            'enrollment_no': '12345',
            'department': 'Computer Science',
            'year': 'Sophomore'
        })
        response = self.client.get('/admin/students')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json['data']), 1)

    def test_get_all_parents(self):
        self.client.post('/parents/', json={
            'name': 'Jane Doe',
            'email': 'jane@example.com',
            'phone': '1234567890',
            'student_id': '607f1f77bcf86cd799439011'
        })
        response = self.client.get('/admin/parents')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json['data']), 1)

if __name__ == '__main__':
    unittest.main()
