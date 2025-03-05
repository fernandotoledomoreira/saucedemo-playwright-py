import json
from pytests.support.hooks import *
from pytests.mocks.api_book_mocks import *
from pytests.clients.api_books_client import ApiBooksClient
from pytests.support.api_utils import ApiUtils
from pytests.examples.examples_api_book import *
from pytests.clients.common import Common
from pytests.schemas.contract_api import *


@pytest.mark.crud_livros
def test_post_livros():
    payload = payload_post_livros()
    ApiUtils.payload_parse_log(payload)
    response = ApiBooksClient.post_livros(payload)
    resp_parse = ApiBooksClient.validate_response(response, 201)
    ApiUtils.validate_json_schema(response, post_api_livraria)

@pytest.mark.crud_livros
@pytest.mark.parametrize("field, value, code", examples_post_livros)
def test_invalid_values_post_livros(field, value, code):
    payload = payload_post_livros()
    payload = Common.change_fields_payload(payload, field, value)
    ApiUtils.payload_parse_log(payload)
    response = ApiBooksClient.post_livros(payload)
    ApiBooksClient.validate_response(response, code)


@pytest.mark.crud_livros
def test_get_all_livros():
    response = ApiBooksClient.get_livros()
    ApiBooksClient.validate_response(response, 200)


@pytest.mark.crud_livros
def test_get_livros_id():
    response = ApiBooksClient.get_livros_id()
    ApiBooksClient.validate_response(response, 200)


@pytest.mark.crud_livros
def teste_patch_livro():
    payload = payload_post_livros()
    ApiUtils.payload_parse_log(payload)
    response = ApiBooksClient.post_livros(payload)
    ApiBooksClient.validate_response(response, 201)
    response_json = json.loads(response['body'])
    id = response_json['id']
    payload = payload_patch_livros()
    ApiUtils.payload_parse_log(payload)
    response = ApiBooksClient.patch_livros_id(id, payload)
    ApiBooksClient.validate_response(response, 200)


@pytest.mark.crud_livros
def teste_put_livro():
    payload = payload_post_livros()
    ApiUtils.payload_parse_log(payload)
    response = ApiBooksClient.post_livros(payload)
    ApiBooksClient.validate_response(response, 201)
    response_json = json.loads(response['body'])
    id = response_json['id']
    payload = payload_put_livros()
    ApiUtils.payload_parse_log(payload)
    response = ApiBooksClient.put_livros_id(id, payload)
    ApiBooksClient.validate_response(response, 200)


@pytest.mark.crud_livros
def teste_delete_livro():
    payload = payload_post_livros()
    ApiUtils.payload_parse_log(payload)
    response = ApiBooksClient.post_livros(payload)
    ApiBooksClient.validate_response(response, 201)
    response_json = json.loads(response['body'])
    id = response_json['id']
    response = ApiBooksClient.delete_livros_id(id)
    ApiBooksClient.validate_response(response, 200)
