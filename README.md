# Taller II Payment API
[![Build Status](https://travis-ci.org/gfusca/taller-ii-payment-api.svg?branch=master)](https://travis-ci.org/gfusca/taller-ii-payment-api)
[![codecov](https://codecov.io/gh/gfusca/taller-ii-payment-api/branch/master/graph/badge.svg)](https://codecov.io/gh/gfusca/taller-ii-payment-api)

API para procesamiento de pagos electronicos

Heroku dyno: https://shielded-escarpment-27661.herokuapp.com

## Endpoints:

### Generación de token

Para la generación de tokens se debe obtener las credenciales (id & secret) que serán otorgadas durante la petición de acceso a la API
```
curl -X POST http://<api_url>/api/v1/user/oauth/authorize \
  -d 'grant_type=client_credentials&client_id=145227&client_secret=12f071174cb7eb79d4aac5bc2f07563f'
```

Response

```
{
    "access_token":"7524f96e-2d22-45da-bc64-778a61cbfc26",
    "token_type":"bearer",
    "expires_in":43199,
    "grant_type":"client_credentials"
} 
```

### Consulta de metodos de pagos disponibles 
  /paymethods

```
curl -X GET http://<api_url>/api/v1/paymethods
    -H "Authorization: Bearer 87ad751f-7ea5-4023-a16f-04b6647a07f5"`
```

Response: 

```
{
  "items": [
    {
      paymethod: "card"
      parameters: {
        "number": "string"
        "type": "string",
        "expirationMonth": "number",
        "expirationYear": "number",
        "ccvv": "number"
      }
    }
  ]
}
```

### Procesamiento de pago

```
curl -X POST http://<api_url>/api/v1/pay
    -H "Authorization: Bearer 87ad751f-7ea5-4023-a16f-04b6647a07f5"
    -d '{
        "transaction-id": null,
        "paymentMethod": {
            "method": "card",
            "number": "484848484848484",
            "type": "visa",
            "expirationMonth": "11",
            "expirationYear": "20",
        },
        "currency": "USD",
        "value": "65.00"
      }'
```

Response:

```
{
  "transaction-id": "550e8400-e29b-41d4-a716-446655440000",
  "paymentMethod": {
      "method": "card",
      "number": "484848484848484",
      "type": "visa",
      "expirationMonth": "11",
      "expirationYear": "20",
  },
  "currency": "USD",
  "value": "65.00"
}
```
