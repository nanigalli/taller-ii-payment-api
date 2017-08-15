from model import postgresql

class Credential(postgresql.Model):
  __tablename__ = "credentials"

  client_id = postgresql.Column(postgresql.String(128), primary_key=True)
  client_secret = postgresql.Column(postgresql.String(128))

  def __init__(self, client_id, client_secret):
    self.client_id = client_id
    self.client_secret = client_secret



