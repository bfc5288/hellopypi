import pytest
from time import sleep

def test_func_fast():
    pass

@pytest.mark.slow
def test_func_slow():
    sleep(3)
    pass
