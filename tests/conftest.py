import os
import pytest
from checker.__main__ import Server


@pytest.fixture(scope='module')
def server() -> Server:
    yield Server()


@pytest.fixture(scope='module')
def _set_api_url() -> None:
    os.environ['AWS_ENDPOINT'] = 'secret'


@pytest.fixture(scope='module')
def _unset_api_url() -> None:
    os.environ['AWS_ENDPOINT'] = ''
