"""Module provides API for application endpoints."""
import os
from typing import Any, Dict
import attr


def api_url() -> str:
    """Returns AWS_ENDPOINT URL."""
    url: str = os.environ.get('AWS_ENDPOINT', '')
    if not url:
        raise RuntimeError('Please set API_URL environment variable')
    return url


@attr.dataclass(frozen=True, slots=True)
class Server:
    """The class represents a server endpoint."""

    host: str = 'localhost'
    port: int = 5050
    is_debug: bool = True
    reloader: bool = True

    def as_json(self) -> Dict[str, Any]:
        """Returns server configuration as a dict."""
        return {
            'host': self.host,
            'port': self.port,
            'is_debug': self.is_debug,
            'reloader': self.reloader,
        }
