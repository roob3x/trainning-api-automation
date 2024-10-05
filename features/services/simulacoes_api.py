from qa_platform.core.utils.fridge import *
from services import *

def post_simulacoes(url, payload):
    headers = {
        'accept': '*/*',
        'Content-Type': 'application/json'
    }
    return do_request("POST", url, headers, payload)


def put_simulacoes(url, payload):
    headers = {
        'accept': '*/*',
        'Content-Type': 'application/json'
    }
    return do_request("PUT", url, headers, payload)