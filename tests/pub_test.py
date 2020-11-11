import unittest
from src.pub import Pub

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("Kings Head", 1000, ["whisky", "vodka", "lager", "cider"])

    def test_pub_has_name(self):
        self.assertEqual("Kings Head", self.pub.name)

    def test_pub_has_money(self):
        self.assertEqual(1000, self.pub.cash)

    def test_has_drinks(self):
        self.assertEqual(["whisky", "vodka", "lager", "cider"], self.pub.drinks)
        
    