import pytest
from unittest.mock import Mock, patch

from wallet import Wallet, InsufficientAmount, grab_bag

@pytest.fixture
def default_wallet():
    '''Returns a wallet with default balance'''
    return Wallet()

@pytest.fixture
def wallet():
    '''Returns a wallet with balance 20'''
    return Wallet(20)


@pytest.fixture(scope="session")
def fixture_one():
    return 'success one'

@pytest.fixture(scope="session")
def fixture_two():
    return 'success two'


# @pytest.fixture()
# def fixture_arg():
#     return 'success one'

# @pytest.fixture()
# def normal_arg():
#     return 'string one'

@pytest.fixture(params=[fixture_one, fixture_two])
def fixture_arg(request):
    return request.getfixturevalue(request.param)

@pytest.mark.parametrize("normal_arg, fixture_arg", [("string_one", fixture_one),("string_two", fixture_two)])
def test_nested_fixtures(normal_arg, fixture_arg):
    assert "string" in normal_arg
    assert fixture_arg == 'success one'




def test_default_amount(default_wallet):
    assert default_wallet.balance == 0, 'Should be 0'
    
def test_init_amount(wallet):
    initial_amt = 20
    assert wallet.balance == initial_amt, f'Should be {initial_amt}'

def test_spend(wallet):
    wallet.spend(10)
    assert wallet.balance == 10, 'Should be 10'
    
def test_spend_insuf(wallet):
    with pytest.raises(InsufficientAmount):
        wallet.spend(30)

def test_add(wallet):
    wallet.add(10)
    assert wallet.balance == 30, 'Should be 30'

@pytest.mark.parametrize('earned,spent,expected', [
    (30,10,20),
    (20,2,18),
    ])

def test_transact(default_wallet,earned,spent,expected):
    default_wallet.add(earned)
    default_wallet.spend(spent)
    assert default_wallet.balance == expected, f'Should be {expected}'


@pytest.fixture
def default_bag():
    '''Grab bag with default cost
    '''
    return grab_bag()

@pytest.fixture
def bag():
    '''Grab bag with cost of 50
    '''
    return grab_bag(50)

def test_default_grab_bag(default_bag):
    assert default_bag.cost == 30, 'Should be 30'

def test_grab_bag(bag):
    assert bag.cost == 50, 'Should be 50'

def test_grab_bag_rand():
    bag = grab_bag()
    treasure = bag.rand_amt()
    assert treasure >= 10, 'Should be a minimum of 10'
    
def test_use_bag(wallet):
    '''Use a mock so that the grab_bag class is never called (so nothing prints), but the use_bag
    method can still be tested.
    '''
    
    grab_bag = Mock()
    grab_bag.get_cost.return_value = 0
    grab_bag.rand_amt.return_value = 0

    print('nothing should be printed after this')
    wallet.use_bag(grab_bag)

    assert wallet.balance == 20, 'Should be 20 since cost and treasure amounts are zero'
