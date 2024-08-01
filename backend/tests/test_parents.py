
import unittest
from app import create_app
from app.models import Parent

class ParentTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.config['MONGO_DBNAME'] = 'testdb'
        self.app.config['TESTING'] = True
        with self.app.app_context():
            self.db = self.app.mongo.db

    def tearDown(self):
        with self.app.app_context():
            self.db.parents.delete_many({})

    def test_add_parent(self):
        response = self.client.post('/parents/', json={
            'name': 'Jane Doe',
            'email': 'jane@example.com',
            'phone': '1234567890',
            'student_id': '607f1f77bcf86cd799439011'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Parent added successfully', response.json['message'])

    def test_get_parents(self):
        self.client.post('/parents/', json={
            'name': 'Jane Doe',
            'email': 'jane@example.com',
            'phone': '1234567890',
            'student_id': '607f1f77bcf86cd799439011'
        })
        response = self.client.get('/parents/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json['data']), 1)

if __name__ == '__main__':
    unittest.main()