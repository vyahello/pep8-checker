import os
import pytest
from checker.endpoint import Server


@pytest.fixture(scope='module')
def server() -> Server:
    yield Server()


@pytest.fixture(scope='module')
def set_api_url() -> str:
    os.environ['AWS_ENDPOINT'] = 'secret'
    yield os.environ['AWS_ENDPOINT']


@pytest.fixture(scope='module')
def unset_api_url() -> str:
    os.environ['AWS_ENDPOINT'] = ''
    yield os.environ['AWS_ENDPOINT']
