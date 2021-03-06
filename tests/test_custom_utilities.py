import unittest
import flask_jwt_extended

from app.utilities import (generate_hash, verify_hash, get_user_info, poor_mans_token_parser, create_tokens)

class TestCustomUtilities(unittest.TestCase):
    def setUp(self):
        self.sample_jwt = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NTMzNjQ2MDEsIm5iZiI6MTU1MzM2NDYwMSwianRpIjoiNGNiODk1N2QtM2I0MS00N2M4LTlmN2ItNGMyODkwZTAzYjhhIiwiZXhwIjoxNTUzMzY1NTAxLCJpZGVudGl0eSI6ImEwZWNhMzlhLTRiZTEtNGMwMS04YzJkLWU3NDgxYWE5ZjllYSIsImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyJ9.fruaZRq5khXChfrnw3PTDERXDveA-h20gJdvJIUpjS0'
        self.password = 'password_12345'
        self.incorrect_password = '12345_password'
        self.identity = '6cdbc440-9056-4470-9f98-e30cf43ab0f0'
        
    def test_generating_hash(self):
        data = generate_hash(self.password)
        self.assertTrue(len(data) > 0)

    def test_verify_hash(self):
        hash_value = generate_hash(self.password)
        data = verify_hash(self.password, hash_value)
        self.assertIsNotNone(data)
        self.assertTrue(data)

    def test_verify_hash_incorrectly(self):
        hash_value = generate_hash(self.password)
        data = verify_hash(self.incorrect_password, hash_value)
        self.assertIsNotNone(data)
        self.assertFalse(data)

    @unittest.expectedFailure
    def test_token_parser(self):
        self.assertIsNotNone(self.sample_jwt)
        decoded = poor_mans_token_parser(token=self.sample_jwt)
        self.assertTrue(len(decoded) > 0)

    @unittest.expectedFailure
    def test_create_tokens(self):
        data = create_tokens(identity=self.identity)
        self.assertTrue(len(data) > 0)

    @unittest.expectedFailure
    def test_get_user_info(self):
        data = get_user_info(token=self.sample_jwt)
        self.assertTrue(len(data) > 0)

    def tearDown(self):
        self.sample_jwt = None
        self.password = None
        self.incorrect_password = None
