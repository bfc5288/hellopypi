#!/opt/conda/bin/python

from unittest.mock import Mock, patch

def cow():
    print('cow')
    return 'moo'

def dog():
    print('dog')
    return 'bark'

def ponies():
    print('ponies')
    return 'pls no'

def animals():
    herd = []
    herd.append(cow())
    herd.append(dog())
    herd.append(ponies())
    herd.append(ponies())
    herd.append('oink')
    return herd

def test_dog():
    assert dog() == 'bark'

def test_cow():
    assert cow() == 'moo'
    
def test_ponies():
    assert ponies == 'pls no'

# note: the order in which patches are passed to a test are latest first. So, dog precedes cow below
# so that the test receives cow first.
@patch('__main__.dog')
@patch('__main__.cow')
def test_animals(patch_cow,patch_dog):
    '''Test animals, but with patches for cow and dog since we don't want them to run. But, we still 
    want to test that `herd` contains all the voices, so we set return values for the patches.
    '''
    patch_cow.return_value='moo'
    patch_dog.return_value='bark'
    herd = animals()
    print(herd)
    assert herd == ['moo','bark','pls no','pls no','oink']
    assert patch_cow.called is True
    assert patch_dog.called is True    

test_animals()
