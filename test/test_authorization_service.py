import requests
import unittest
from main import app

class AuthorizationServiceTestCase(unittest.TestCase):

  def test_create_acces_token_without_header_returns_403(self):
    endpoint = "/api/v1/user/oauth/authorize"
    tester = app.test_client(self)
    response= tester.post(endpoint, data={})
    self.assertEqual(response.status_code, 403)
