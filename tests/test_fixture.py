import pytest

@pytest.fixture
def some_vars():
    a = 1
    b = 2
    c = 3
    return [a,b,c]

def test_one(some_vars):
    a = some_vars[0]
    b = some_vars[1]
    assert a + 1 == b

def test_two(some_vars):
    d = 4
    c = some_vars[2]
    assert d == c + 1

def test_three(more_vars):
    assert more_vars[0] == more_vars[1] - 1

def test_four(some_vars,more_vars):
    a=some_vars[0]
    z=more_vars[2]
    assert a == z
