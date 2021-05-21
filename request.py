import requests


REQUEST_HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
REQUEST_TIMEOUT = 30


class Request:

    def __init__(self):
        self.headers = REQUEST_HEADERS
        self.timeout = REQUEST_TIMEOUT

    def get_status_code(self, url):
        response = self.head(url)
        return response.status_code

    def get_text_response(self, url):
        response = self.get(url)
        return response.text

    def get_json_response(self, url):
        response = self.get(url)
        return response.json()

    def head(self, url):
        return requests.head(url, headers=REQUEST_HEADERS, timeout=REQUEST_TIMEOUT)

    def get(self, url):
        return requests.get(url, headers=REQUEST_HEADERS, timeout=REQUEST_TIMEOUT)
