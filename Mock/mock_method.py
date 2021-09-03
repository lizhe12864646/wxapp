import requests

def send_request(url):
    return requests.get(url).status_code

def invoke_method(url):
    return send_request(url)