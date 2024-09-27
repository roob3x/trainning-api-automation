from qa_platform.core.utils.factory import *
from services import *

def post_simulacoes(url, payload):
    headers = {
        'accept': '*/*',
        'Content-Type': 'application/json'
    }
    return do_request("POST", url, headers, payload)