"""Represents executable entrypoint for `pep8-checker` application."""
from typing import Any, Dict, Optional
from pathlib import Path
from bottle import TEMPLATE_PATH, abort, request, route, run, view
import requests
from checker.endpoint import Server, api_url

TEMPLATE_PATH.append(str(Path('./') / 'checker' / 'views'))


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
                code=400,
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
