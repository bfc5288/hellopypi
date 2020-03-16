import pytest

# @pytest.mark.set1
# def test_assert():
#     x = 5
#     y = 6
#     assert x+1 == y

@pytest.mark.parametrize('input1,input2,output',[(5,5,10),(1,2,5)])
def test_add(input1,input2,output):
    assert input1+input2 == output
