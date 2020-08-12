from checker.endpoint import Server
from tests.markers import unit

pytestmark = unit


def test_server_host(server: Server) -> None:
    assert server.host == 'localhost'


def test_server_port(server: Server) -> None:
    assert server.port == 5050


def test_server_debug(server: Server) -> None:
    assert server.is_debug


def test_server_reloader(server: Server) -> None:
    assert server.reloader


def test_server_as_json(server: Server) -> None:
    assert server.as_json() == {
        'host': 'localhost', 'port': 5050, 'is_debug': True, 'reloader': True
    }


def test_api_url_set(set_api_url: str) -> None:
    assert set_api_url


def test_api_url_unset(unset_api_url: str) -> None:
    assert not unset_api_url
