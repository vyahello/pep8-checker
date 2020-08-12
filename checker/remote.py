"""Represents executable entrypoint for AWS lambda function."""
from contextlib import redirect_stdout
from io import StringIO
from tempfile import NamedTemporaryFile as temp_file
from typing import Any, Dict
import pycodestyle


def lambda_handler(event: Dict[str, Any]) -> Dict[str, Any]:
    """Returns response from AWS lambda execution."""
    code: str = event.get('code', '')
    with open(temp_file(dir='/tmp').name, 'w') as file:
        file.write(f'{code}\n')
        file.seek(0)
        output = StringIO()
        with redirect_stdout(output):
            pep = pycodestyle.Checker(filename=file.name, show_source=True)
            pep.check_all()
        return {'statusCode': 200, 'body': output.getvalue()}


def call_bad_event() -> Dict[str, Any]:
    """Returns bad code event."""
    return lambda_handler(event={'code': '    print("hello world")'})


def call_good_event() -> Dict[str, Any]:
    """Returns good code event."""
    return lambda_handler(event={'code': 'print("hello world")'})


if __name__ == '__main__':
    call_good_event()
    call_bad_event()
