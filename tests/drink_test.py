import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Fosters", 5)

    def test_drink(self):
        self.assertEqual("Fosters", self.drink.name)

    def test_price(self):
        self.assertEqual(5, self.drink.price)

