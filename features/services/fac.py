from qa_platform.core.utils.fridge import *
from hamcrest import assert_that, is_

def load_schema(schema):
    return get_fixtures(schema)


def get_response(response):
    res = response.json()
    return res

def validate_status_code(context, status_code):
    assert_that(context.response.status_code, is_(int(status_code)))


def get_message_from_response(response, message):
    return response[f'{message}']