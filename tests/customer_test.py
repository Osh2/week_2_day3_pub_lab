import unittest 
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Jack", 40)

    def test_customer_has_name(self):
        self.assertEqual("Jack", self.customer.name)

    def test_customer_has_money(self):
        self.assertEqual(40, self.customer.wallet)
        