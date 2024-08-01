import unittest
from app import create_app
from app.models import Event

class EventTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.config['MONGO_DBNAME'] = 'testdb'
        self.app.config['TESTING'] = True
        with self.app.app_context():
            self.db = self.app.mongo.db

    def tearDown(self):
        with self.app.app_context():
            self.db.events.delete_many({})

    def test_add_event(self):
        response = self.client.post('/events/', json={
            'name': 'Hackathon',
            'description': '24-hour coding event',
            'date': '2024-07-31'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Event added successfully', response.json['message'])

    def test_get_events(self):
        self.client.post('/events/', json={
            'name': 'Hackathon',
            'description': '24-hour coding event',
            'date': '2024-07-31'
        })
        response = self.client.get('/events/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json['data']), 1)

if __name__ == '__main__':
    unittest.main()
