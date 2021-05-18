import requests


REQUEST_HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
REQUEST_TIMEOUT = 10

class BrokenLinkChecker:
    
    def __init__(self, link):
        self.link = link

    def is_broken(self):
        try:
            self.link.clean()
            response = requests.head(self.link.url, headers=REQUEST_HEADERS, timeout=REQUEST_TIMEOUT)
            if response.status_code == 404:
                return True

            return False
        except Exception as e:
            print(f'Error checking status code for {url}')
            raise e