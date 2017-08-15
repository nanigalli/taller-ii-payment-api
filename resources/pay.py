from flask_restful import Resource
from flask import jsonify, make_response, request
import uuid
from models.token import Token


class InvalidAuthTypeException(Exception):
  pass
class InvalidTokenException(Exception):
  pass

def auth(authtype, token):
  if (authtype != "Bearer" and authtype != "bearer"):
    raise InvalidAuthTypeException("Authorization type must be bearer!")
  if ( not Token.exists(token)):
    raise InvalidTokenException("Invalid authorization token!")  

class Pay(Resource):
  def post(self):
    authtype, token = request.headers.get('Authorization').split()
    try:
      auth(authtype, token)
      transaction_id = str(uuid.uuid4())
      return make_response(
        jsonify(
          {
            "transaction-id": transaction_id,
            "paymentMethod": {
                "card": {
                 "number": "484848484848484",
                 "type": "visa",
                 "expirationMonth": "11",
                 "expirationYear": "20",
              }
            },
            "currency": "USD",
            "value": "65.00"
          } 
        )
      )
    except (InvalidAuthTypeException, InvalidTokenException) as e:
      return make_response(jsonify(
        {
          "status_code": 403,
          "message": e.message
        }
      ))
