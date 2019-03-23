import unittest
from app.People.service import PeopleService

class TestPeopleService(unittest.TestCase):
    def setUp(self):
        self.service = PeopleService()
        self._id = '6cdbc440-9056-4470-9f98-e30cf43ab0f0'
        self.data = self.service.fetch(self._id)
    
    def test_fetch_all(self):
        self.assertIsNotNone(self.service)
        limit = 2
        search_value = self.service.fetch_all(limit=limit)
        self.assertTrue(len(search_value) > 0 and len(search_value) <= limit)

    def test_fetch_one(self):
        self.assertIsNotNone(self.data)

    @unittest.expectedFailure
    def test_fetch_team(self):
        self.assertIsNotNone(self.data)
        team_values = self.service.fetch_team(person=self.data[0])
        self.assertIsNotNone(team_values)

    @unittest.expectedFailure
    def test_fetch_manager(self):
        self.assertIsNotNone(self.data)
        team_values = self.service.fetch_manager(person=self.data[0])
        self.assertIsNotNone(team_values)

    def tearDown(self):
        self.service = None
        self._id = None
        self.data = None
        
