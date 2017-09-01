from model import postgresql
from sqlalchemy import Integer, ForeignKey, String, Column, Numeric
from sqlalchemy.orm import relationship, backref
from models.paymeythod import PayMethod


class Payment(postgresql.Model):
  __tablename__ = "payments"

  #TODO: add client_id to transaction table
  

  transaction_id = postgresql.Column(postgresql.String(128), primary_key=True)
  value = postgresql.Column(postgresql.Numeric(10,2, nullable=False)
  currency = postgresql.Column(postgresql.String(3), nullable=False) 
  paymethod = postgresql.Column(postgresql.String(16), ForeignKey('paymethods.paymethod_type'))
  parameters = relationship('PaymentParameter', backref='payments')

  def __init__(self, paymethod, value, currency)
    self.paymethod = paymethod
    self.value = value
    self.currency = currency    

  @staticmethod
  def create(token, value, currency, paymethod):
    curr_session = postgresql.session
    try:
      payment = Payment._create_payment(paymethod['method'], value, currency, paymethod, curr_session)
      curr_session.commit()
      return payment
    except Exception as e:
        curr_session.rollback()
        curr_session.flush()
        return None
    return None

  def _create_payment(paymethod, value, currency, parameters, curr_session):
    import uuid
    transaction_id = str(uuid.uuid4())
    payment = Payment(paymethod['method'], value, currency)
    curr_session.add(payment)
    Payment._add_parameters(transaction_id, paymethod, curr_session)
    return payment

  def _add_parameters(transaction_id, paymethod, curr_session):
    inserted = []
    for k,v in paymethod.iteritems():
      if k is not "method":
        parameter = PaymentParameter(transaction_id, key, value)
        curr_session.add(parameter)
    return paymethod


class PaymentParameter(postgresql.Model):
  __tablename__ = "payment_parameters"

  payment_parameter_id = postgresql.Column(Integer, primary_key=True)
  payment_parameter_name =  postgresql.Column(postgresql.String(16))
  payment_parameter_value = postgresql.Column(postgresql.String(128))
  transaction_id = postgresql.Column(postgresql.String(128), ForeignKey('payments.transaction_id'))

  def __init__(self, transaction_id, name, value):
    self.transaction_id = transaction_id
    self.payment_parameter_name = name
    self.payment_parameter_value = value

