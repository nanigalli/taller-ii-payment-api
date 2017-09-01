from flask_restful import Resource
from flask import request
from auth import Authorization, InvalidAuthTypeException, InvalidTokenException
from response_builder import build_response
from resources.error_handler import create_error_response
from models.payment import Payment

class Pay(Resource):
  def post(self):
    try:
      authtype, token = self._get_request_headers(request)
      Authorization.auth(authtype, token)
      return self._create_transaction(token)

    except (InvalidAuthTypeException, InvalidTokenException) as e:
      return create_error_response(403, e.message)

  def _create_transaction(self, token):
    value, currency, paymethod = self._get_payment_from_request()
    payment = Payment.create(token, value, currency, paymethod)
    return build_response(
          {
            "transaction-id": transaction_id,
            "paymentMethod": {
              "method": "card",
              "number": parameters['number'],
              "type": parameters['type'],
              "expirationMonth": parameters['expiration_month'],
              "expirationYear": parameters['expiration_year']
            },
            "currency": "USD",
            "value": "65.00"
          }, 201
    )

  def _get_payment_from_request(self):
    body = request.json()
    paymethod = body['paymentMethod']
    return body['value'], body['currency'], paymethod 

  def _get_request_headers(request):
    return request.headers.get('Authorization').split()
