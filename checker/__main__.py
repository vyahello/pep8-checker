"""Represents executable entrypoint for `pep8-checker` application."""
import http
import os
from typing import Any, Dict, Optional
from pathlib import Path
import attr
from bottle import TEMPLATE_PATH, abort, request, route, run, view
import requests

TEMPLATE_PATH.append(str(Path('./') / 'checker' / 'views'))


def api_url() -> str:
    """Returns AWS_ENDPOINT URL."""
    url: str = os.environ.get('AWS_ENDPOINT', '')
    if not url:
        raise RuntimeError('Please set API_URL environment variable')
    return url


@attr.dataclass(frozen=True, slots=True)
class Server:
    """The class represents a server endpoint."""

    host: str = '0.0.0.0'
    port: str = os.environ.get('PORT', '5050')
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


@route('/', method=('GET', 'POST'))
@view(tpl_name='index')
def index() -> Dict[str, str]:
    """Specify index page view.

    Returns: <dict[str, str]> response from AWS lambda server.
    """
    title = 'PEP8 Checker'
    code: str = request.forms.get('code', '')  # pylint: disable=no-member
    if code:
        resp: Dict[Any, Any] = requests.post(
            url=api_url(), json={'code': code}
        ).json()
        error: Optional[str] = resp.get('errorMessage')
        exception: Optional[str] = resp.get('errorType')
        if error and exception:
            abort(
                code=int(http.HTTPStatus.BAD_REQUEST),
                text=f'Lambda function returned status {exception} exception',
            )
        return {'title': title, 'code': code, 'pep_errors': resp['body']}
    return {'title': title, 'code': code, 'pep_errors': ''}


def easyrun(server: Server = Server()) -> None:
    """Launches a web application.

    Args:
        server: <Server> a given server configuration.
    """
    run(
        host=server.host,
        port=server.port,
        debug=server.is_debug,
        reloader=server.reloader,
    )


if __name__ == '__main__':
    easyrun()
