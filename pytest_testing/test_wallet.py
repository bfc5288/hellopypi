import pytest
from wallet import Wallet, InsufficientAmount

def test_default_amount():
    my_wallet = Wallet()
    assert my_wallet.balance == 0, 'Should be 0'
    
def test_init_amount():
    initial_amt = 50
    my_wallet = Wallet(initial_amt)
    assert my_wallet.balance == initial_amt, f'Should be {initial_amt}'


def test_spend():
    my_wallet = Wallet(20)
    my_wallet.spend(10)
    assert my_wallet.balance == 10, 'Should be 10'
    
def test_spend_insuf():
    my_wallet = Wallet()
    with pytest.raises(InsufficientAmount):
        my_wallet.spend(10)

def test_add():
    my_wallet = Wallet()
    my_wallet.add(10)
    assert my_wallet.balance == 10, 'Should be 10'
