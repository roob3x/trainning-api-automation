from qa_platform.core.utils.fridge import *

def load_schema(schema):
    return get_fixtures(schema)


def get_response(response):
    res = response.json()
    return res

def get_status_code(response):
    return response.status_code