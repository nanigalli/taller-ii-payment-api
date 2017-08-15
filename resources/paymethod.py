from flask_restful import Resource
from flask import jsonify, make_response


class PayMethod(Resource):
  def get(self):
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

