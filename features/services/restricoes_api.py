from qa_platform.core.utils import do_request
from support import endpoints.yml

def get_restricoes(url):
    headers = ""
    payload = ""
    return do_request("GET", url, headers, payload)