from flask_restful import Resource
from flask import request

from auth import Authorization, InvalidAuthTypeException, InvalidTokenException
from models.paymethod import PayMethod
from response_builder import build_response
from resources.error_handler import create_error_response


class PayMethodResource(Resource):
  def get(self):
    try:
      authtype, token = self._get_authorization_header(request)
      Authorization.auth(authtype, token)
      paymethod = PayMethod()
      methods = paymethod.get_all()
      return self._create_get_response(methods)

    except (InvalidAuthTypeException, InvalidTokenException) as e:
      status_code = 403
      message = e.message
      return create_error_response(status_code, msg)

  def _get_authorization_header(self, request):
      return request.headers.get('Authorization').split()

  def _create_get_response(self, methods):
    payment_response = {
      "items": []
    }
    
    for m in methods:
      item = {
        "paymethod": m.paymethod_type,
        "parameters": {}
      }
      for p in m.parameters:
        item['parameters'].update({p.parameter_name: p.parameter_value_type})
      
      payment_response['items'].append(item)
    return build_response(payment_response)
