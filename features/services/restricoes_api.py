from qa_platform.core.utils.fridge import *

def get_restricoes(url):
    headers = ""
    payload = ""
    return do_request("GET", url, headers, payload)

