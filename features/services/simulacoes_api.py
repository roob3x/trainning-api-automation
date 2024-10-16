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

def get_simulacao(url):
    headers = {
        'accept': '*/*',
        'Content-Type': 'application/json'
    }
    payload = ""
    return do_request("GET", url, headers, payload)

def del_simulacao(url):
    headers = {
        'accept': '*/*',
    }
    payload = ""
    return do_request("DELETE", url, headers, payload)
    
