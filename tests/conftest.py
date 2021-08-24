import os, pytest

@pytest.fixture(scope="session")
def fixture_setups():
    print("hello")
    os.environ['DATABASE_URL'] = 'My super test name| Python version {}'.format(python_version)
