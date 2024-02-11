from pytest import raises
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError
from .tag_creator_validator import tag_creator_validator

class MockRequest:
    def __init__(self, json) -> None:
        self.json = json

def test_tag_creator_validator():
    req = MockRequest(json={
        "product_code": "12345"
    })

    tag_creator_validator(req)

def test_tag_creator_validator_failed():
    req = MockRequest(json={
        "product_code": 12345
    })

    # Duas formas de se fazer:
        # A primeira é a mais correta, a segunda é mais "gambiarra"

    with raises(HttpUnprocessableEntityError):
        tag_creator_validator(req)

    # try:
    #     tag_creator_validator(req)
    #     assert False
    # except Exception as exception:
    #     assert isinstance(exception, HttpUnprocessableEntityError)
