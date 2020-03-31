import pytest


def capital_case(x):
    if not isinstance(x, str):
        raise TypeError('Please provide a string argument')
    
    return x.capitalize()

def test_capital_case():
    assert capital_case('hello!') == 'Hello!'

def test_capital_non_str():
    with pytest.raises(TypeError):
        capital_case(9)
        
