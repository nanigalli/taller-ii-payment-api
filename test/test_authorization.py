from resources.authorization import AuthorizationResource
from models.token import Token
import mock 
import unittest
from flask import Flask, jsonify

class AuthorizationResourceTestCase(unittest.TestCase):

  def test_authorization(self):
    response = {
      "access_token": "994c1464-3f4c-4077-9253-656d32dc88fb",
      "expires_in": "1504028964",
      "grant_type": "client_credentials",
      "token_type": "bearer"
    }
    service = AuthorizationResource()
    service._get_client_id_from_request = mock.MagicMock(return_value='ee04c1bd-bd98-4ac9-861e-cff1834e0386')
    service._get_client_secret_from_request = mock.MagicMock(return_value='1e238cae-26ae-412d-a7e6-959e89980a13')
    service._create_access_token_response = mock.MagicMock(return_value=response)
    jsonify = mock.MagicMock(return_value=response)
    Token.create = mock.MagicMock(
      return_value = {
        "access_token": "994c1464-3f4c-4077-9253-656d32dc88fb",
        "expiration": "1504028964"
      }
    )
    self.assertEqual(service.post(), response)
