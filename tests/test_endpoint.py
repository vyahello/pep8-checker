import pytest
from checker.__main__ import Server, api_url
from tests.markers import unit

pytestmark = unit


def test_server_host(server: Server) -> None:
    assert server.host == '0.0.0.0'


def test_server_port(server: Server) -> None:
    assert server.port == '5050'


def test_server_debug(server: Server) -> None:
    assert server.is_debug


def test_server_reloader(server: Server) -> None:
    assert server.reloader


def test_server_as_json(server: Server) -> None:
    assert server.as_json() == {
        'host': '0.0.0.0', 'port': '5050', 'is_debug': True, 'reloader': True
    }


@pytest.mark.usefixtures('_set_api_url')
def test_api_url_set() -> None:
    assert api_url()


@pytest.mark.usefixtures('_unset_api_url')
def test_api_url_unset() -> None:
    with pytest.raises(RuntimeError):
        api_url()
