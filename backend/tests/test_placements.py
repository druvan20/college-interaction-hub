import unittest
from app import create_app
from app.models import Placement

class PlacementTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.config['MONGO_DBNAME'] = 'testdb'
        self.app.config['TESTING'] = True
        with self.app.app_context():
            self.db = self.app.mongo.db

    def tearDown(self):
        with self.app.app_context():
            self.db.placements.delete_many({})

    def test_add_placement(self):
        response = self.client.post('/placements/', json={
            'company': 'Google',
            'position': 'Software Engineer',
            'description': 'Work on various projects',
            'date': '2024-07-31'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Placement added successfully', response.json['message'])

    def test_get_placements(self):
        self.client.post('/placements/', json={
            'company': 'Google',
            'position': 'Software Engineer',
            'description': 'Work on various projects',
            'date': '2024-07-31'
        })
        response = self.client.get('/placements/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json['data']), 1)

if __name__ == '__main__':
    unittest.main()
