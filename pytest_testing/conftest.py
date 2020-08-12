import pytest




# for cli option parsing in test_cliopt.py

@pytest.fixture
def cmdopt(request):
    return request.config.getoption('--cli_opt')

# for skipping tests marked as slow

def pytest_configure(config):
    config.addinivalue_line('markers', 'slow: mark test as slow to run')

def pytest_collection_modifyitems(config, items):
    if config.getoption('--runslow'):
        # --runslow is given in cli, so do not skip slow tests
        return
    # otherwise, mark the test to skip
    skip_slow = pytest.mark.skip(reason='specify --runslow option to run')
    for item in items:
        if 'slow' in item.keywords:
            item.add_marker(skip_slow)

