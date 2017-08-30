from flask_restful import Resource
from flask import jsonify, make_response, request
import uuid
from auth import Authorization, InvalidAuthTypeException, InvalidTokenException


class Pay(Resource):
  def post(self):
    authtype, token = request.headers.get('Authorization').split()
    try:
      Authorization.auth(authtype, token)
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
