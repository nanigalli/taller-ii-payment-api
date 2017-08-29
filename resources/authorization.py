from flask_restful import Resource
from flask import request
from models.token import Token
from flask import jsonify, make_response

class AuthorizationResource(Resource):

  def post(self):
    client_id = self._get_client_id_from_request()
    client_secret = self._get_client_secret_from_request()
    return self._create_access_token_response(Token.create(client_id, client_secret))

  def _get_client_id_from_request(self):
    return request.get_json()['client_id']

  def _get_client_secret_from_request(self):
    return request.get_json()['client_secret']

  def _create_access_token_response(self, token):
    response = None
    try:
      response = make_response(
        jsonify(
          {
            "access_token": token.access_token,
            "token_type":"bearer",
            "expires_in": token.expiration,
            "grant_type":"client_credentials"
          }
        ), 201
      )
    except:
      status_code = 403
      response = make_response(
        jsonify(
          {
            "status_code": status_code,
            "message": "Cannot create tokens, invalid credentials"
          }
        ), status_code
      )
    return response
