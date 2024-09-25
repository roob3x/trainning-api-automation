from qa_platform.core.utils.factory import *

def get_restricoes(url):
    headers = ""
    payload = ""
    return do_request("GET", url, headers, payload)

def load_schema(schema):
    return get_fixtures(schema)