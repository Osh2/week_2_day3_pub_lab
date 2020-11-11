import unittest 
from src.customer import Customer
from src.pub import Pub
from src.drink import Drink
class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Jack", 40)

    def test_customer_has_name(self):
        self.assertEqual("Jack", self.customer.name)

    def test_customer_has_money(self):
        self.assertEqual(40, self.customer.wallet)
        
    def test_customer_can_buy_drink(s)