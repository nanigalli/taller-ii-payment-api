from models.token import Token

class InvalidAuthTypeException(Exception):
  pass
class InvalidTokenException(Exception):
  pass

class Authorization:

  @staticmethod
  def auth(authtype, token):
    if (authtype != "Bearer" and authtype != "bearer"):
      raise InvalidAuthTypeException("Authorization type must be bearer!")
    if ( not Token.exists(token)):
      raise InvalidTokenException("Invalid authorization token!")
