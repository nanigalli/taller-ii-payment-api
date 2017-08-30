from model import postgresql
from sqlalchemy import Integer, ForeignKey, String, Column, Integer
from sqlalchemy.orm import relationship


class PayMethod(postgresql.Model):
  __tablename__ = "paymethods"

  paymethod_type = postgresql.Column('type', postgresql.String(16), primary_key=True)
  parameters = relationship('PayMethodParameter', backref='paymethods')

  def get_by_type(self, paymethod_type):
    curr_session = postgresql.session #open database session
    return curr_session.query(PayMethod).filter_by(paymethod_type=paymethod_type).first()

  def get_all(self):
    curr_session = postgresql.session #open database session
    return curr_session.query(PayMethod).all()

class PayMethodParameter(postgresql.Model):
  __tablename__ = "paymethod_parameters"

  parameter_id = postgresql.Column('id', Integer, primary_key=True)
  paymethod_type = postgresql.Column(postgresql.String(16), ForeignKey('paymethods.type'))
  parameter_name =  postgresql.Column(postgresql.String(128))
  parameter_value_type = postgresql.Column(postgresql.String(16))

