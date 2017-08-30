from resources.paymethod import PayMethodResource
from mocks.paymethods_mock import paymethod_response_mock
from resources.auth import Authorization
from models.paymethod import PayMethod

import mock 
import unittest

class PayMethodServiceTestCase(unittest.TestCase):

  def test_get_payment_methods(self):
    Authorization.auth = mock.MagicMock(return_value=None)
    PayMethod.get_all = mock.MagicMock(return_value=None)
    service = PayMethodResource()
    service._create_get_response = mock.MagicMock(return_value=paymethod_response_mock)
    service._get_authorization_header = mock.MagicMock(return_value=('Bearer', 'token'))
    self.assertEqual(service.get(), paymethod_response_mock)
