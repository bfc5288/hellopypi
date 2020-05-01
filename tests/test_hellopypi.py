import pytest

@pytest.mark.testing
def test_hellopypi(script_runner):
    ret = script_runner.run('hellopypi', '--version')
    assert ret.success
    
