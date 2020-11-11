import unittest
from src.pub import Pub
from src.drink import Drink
class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("Kings Head", 1000)

    def test_pub_has_name(self):
        self.assertEqual("Kings Head", self.pub.name)

    def test_pub_has_money(self):
        self.assertEqual(1000, self.pub.cash)
   
    def test_has_drinks(self):
        drink1=Drink("Fosters", 10)
        self.pub.add_drink(drink1)
        self.assertEqual(1, len(self.pub.drinks))