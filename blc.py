from request import Request


class BrokenLinkChecker:
    
    def __init__(self):
        self.request = Request()

    def is_broken(self, url):
        try:
            status_code = self.request.get_status_code(url)
            if status_code == 404:
                return True

            return False
        except Exception as e:
            print(f'Error checking status code for {url}')
            raise e