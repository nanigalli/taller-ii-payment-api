from resources.authorization import AuthorizationResource
from models.token import Token
import mock 
import unittest
from mocks.authorization_response import authorization_response
from mocks.token_create_mock import token_creation_mock

class AuthorizationResourceTestCase(unittest.TestCase):

  def test_authorization(self):
    service = AuthorizationResource()
    service._get_client_id_from_request = mock.MagicMock(return_value='ee04c1bd-bd98-4ac9-861e-cff1834e0386')
    service._get_client_secret_from_request = mock.MagicMock(return_value='1e238cae-26ae-412d-a7e6-959e89980a13')
    service._create_access_token_response = mock.MagicMock(return_value=authorization_response)
    jsonify = mock.MagicMock(return_value=authorization_response)
    Token.create = mock.MagicMock(return_value = token_creation_mock)
    self.assertEqual(service.post(), authorization_response)
