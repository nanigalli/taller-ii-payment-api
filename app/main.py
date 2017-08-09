from flask import Flask
from flask import jsonify

app = Flask(__name__)

prefix = "/api/v1"

@app.route('{}/user/oauth/authorize'.format(prefix), methods=['POST'])
def authorize():
  return jsonify({
      "access_token":"7524f96e-2d22-45da-bc64-778a61cbfc26",
      "token_type":"bearer",
      "expires_in":43199,
      "grant_type":"client_credentials"
    } 
  )

@app.route('{}/pay'.format(prefix), methods=['POST'])
def pay():
  return jsonify({
      "transaction-id": "550e8400-e29b-41d4-a716-446655440000",
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

@app.route('{}/paymethods'.format(prefix), methods=['GET'])
def get_pay_methods():
  return jsonify({
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
