import unittest
from app.People.service import PeopleService

service = PeopleService()


class TestPeopleService(unittest.TestCase):
    def test_fetch_all(self):
        self.assertIsNotNone(service)
        limit = 2
        search_value = service.fetch_all(limit=limit)
        self.assertTrue(len(search_value) > 0 and len(search_value) <= limit)

    def test_fetch_one(self):
        self.assertIsNotNone(service)
        _id = '6cdbc440-9056-4470-9f98-e30cf43ab0f0'
        item_value = service.fetch(_id)
        self.assertIsNotNone(item_value)

    def test_fetch_team(self):
        _id = '6cdbc440-9056-4470-9f98-e30cf43ab0f0'
        item_value = service.fetch(_id)
        self.assertIsNotNone(item_value)
        
