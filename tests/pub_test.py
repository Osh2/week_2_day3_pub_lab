import unittest
from src.pub import Pub

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("Kings Head", 1000)

    def test_pub_has_name(self):
        self.assertEqual("Kings Head", self.pub.name)