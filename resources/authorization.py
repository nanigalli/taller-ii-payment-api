from flask_restful import Resource
from flask import request

from models.token import Token
from resources.error_handler import create_error_response
from response_builder import build_response

class AuthorizationResource(Resource):

  def post(self):
    response = None
    try:
      client_id = self._get_client_id_from_request()
      client_secret = self._get_client_secret_from_request()
      response = self._create_access_token_response(Token.create(client_id, client_secret))
    except Exception as e: 
      status_code = 403
      msg = "Cannot create tokens, invalid credentials"
      response = create_error_response(status_code, msg)
    return response

  def _get_client_id_from_request(self):
    return request.get_json()['client_id']

  def _get_client_secret_from_request(self):
    return request.get_json()['client_secret']

  def _create_access_token_response(self, token):
    return build_response({
            "access_token": token.access_token,
            "token_type":"bearer",
            "expires_in": token.expiration,
            "grant_type":"client_credentials"
          }
        , 201
    )
