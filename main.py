from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy
from models.model import postgresql
from models.token import Token
from flask_restful import Resource, Api
import os
from resources.authorization import AuthorizationResource
from resources.paymethod import PayMethod
from resources.pay import Pay

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', '')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

prefix = "/api/v1"

api.add_resource(AuthorizationResource, '{}/user/oauth/authorize'.format(prefix))
api.add_resource(PayMethod, '{}/paymethods'.format(prefix))
api.add_resource(Pay, '{}/pays'.format(prefix))

postgresql.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)

