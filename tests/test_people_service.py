import unittest
from app.People.service import PeopleService

service = PeopleService()


class TestPeopleService(unittest.TestCase):
    def test_search(self):
        self.assertIsNotNone(service)
        query, limit = 'Sipho', 5
        search_value = service.filter(query=query, limit=limit)
        self.assertTrue(len(search_value) > 0)
