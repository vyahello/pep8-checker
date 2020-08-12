from checker.remote import call_bad_event, call_good_event, lambda_handler
from tests.markers import unit

pytestmark = unit


def test_lambda_handler() -> None:
    assert not lambda_handler(event={'code': 'print("hello world")'})['body']


def test_call_bad_event() -> None:
    assert call_bad_event()['body']


def test_call_good_event() -> None:
    assert not call_good_event()['body']
