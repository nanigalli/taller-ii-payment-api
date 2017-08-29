from flask_restful import Resource
from flask import jsonify, make_response, request
from auth import auth, InvalidAuthTypeException, InvalidTokenException


class PayMethod(Resource):
  def get(self):
    try:
      authtype, token = request.headers.get('Authorization').split()
      auth(authtype, token)
      return make_response(
        jsonify({
        "items": [
          {
            "paymethod": "card",
            "parameters": {
              "number": "string",
              "type": "string",
              "expirationMonth": "number",
              "expirationYear": "number",
              "ccvv": "number"
            }
          }
        ]
      })
    )
    except (InvalidAuthTypeException, InvalidTokenException) as e:
      return make_response(jsonify(
        {
          "status_code": 403,
          "message": e.message
        }
      ))
