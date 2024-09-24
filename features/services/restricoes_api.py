from qa_platform.core.utils.factory import do_request

def get_restricoes(url):
    headers = ""
    payload = ""
    return do_request("GET", url, headers, payload)