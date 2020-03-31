from random import random

class InsufficientAmount(Exception):
    pass


class Wallet(object):

    def __init__(self, initial_amount=0):
        self.balance=initial_amount

    def spend(self, amount):
        if self.balance < amount:
            raise InsufficientAmount(f'Not enough funds to spend ${amount}')
        self.balance -= amount

    def add(self, amount):
        self.balance += amount

    def use_bag(self, grab_bag):
        self.spend(grab_bag.get_cost())
        self.add(grab_bag.rand_amt())
        

class grab_bag(object):

    def __init__(self, cost=30):
        self.cost=cost
        print('Your treasure bag is ready')

    def get_cost(self):
        return self.cost
    
    def rand_amt(self):
        print('Spin the wheel for the treasure to take!')
        amt = int(random()*100+10)
        return amt
