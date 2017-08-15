from flask_restful import Resource
from flask import request
from models.token import Token
from flask import jsonify, make_response

class Authorization(Resource):

  def post(self):
    client_id = request.get_json()['client_id']
    client_secret = request.get_json()['client_secret']
    token = Token.create(client_id, client_secret)
    if (token):
      return make_response(
        jsonify(
          {
            "access_token": token.access_token,
            "token_type":"bearer",
            "expires_in": token.expiration,
            "grant_type":"client_credentials"
          }
        ), 201
      )
    else:
      status_code = 403
      return make_response(
        jsonify(
          {
            "status_code": status_code,
            "message": "Cannot create tokens, invalid credentials"
          }
        ), status_code
      )

