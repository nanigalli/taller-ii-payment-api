from model import postgresql
from credential import Credential
from sqlalchemy import and_

expiration_time = 1800

class Token(postgresql.Model):
  __tablename__ = "tokens"

  access_token = postgresql.Column(postgresql.String(128), primary_key=True)
  client_id = postgresql.Column(postgresql.String(128))
  expiration = postgresql.Column(postgresql.String(16))

  def __init__(self, access_token, client_id, expires_in):
    self.access_token = access_token
    self.client_id = client_id
    self.expiration = expires_in

  @staticmethod
  def exists(access_token):
    curr_session = postgresql.session #open database session
    return curr_session.query(Token).filter_by(access_token=access_token).first() is not None


  @staticmethod
  def create(client_id, client_secret):
    import uuid
    import time
    access_token = str(uuid.uuid4())
    expires_in = int(time.time() + expiration_time)
    token = Token(access_token, client_id, expires_in)
    curr_session = postgresql.session #open database session
    try:
        credential = Credential(client_id, client_secret)
        if (curr_session.query(Credential).filter_by(client_id = client_id).filter_by(client_secret = client_secret)):
          token = curr_session.query(Token).filter_by(client_id=client_id).first()
          if (token):
            token.expiration = expires_in
          else:
            curr_session.add(token) #add prepared statment to opened session
          curr_session.commit() #commit changes
        return token
    except Exception as e:
        print e
        curr_session.rollback()
        curr_session.flush() # for resetting non-commited .add()
        return None
    return None

