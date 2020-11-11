from src.pub import Pub

class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def buy_drink(self, pub, drink):
        self.pub.drink.pop()
        self.wallet -= drink.price
        self.pub.cash += drink.price
