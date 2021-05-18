from urllib import parse


class Link:
    
    def __init__(self, url):
        self.url = url
        self.domain = self.get_domain()

    def get_url(self):
        return self.url

    def clean(self):

        if self.url.endswith('.') or self.url.endswith('\'') or self.url.endswith('\\') or self.url.endswith('"'):
            self.url = self.url[:len(self.url)-1]

        if self.url.endswith('&quot'):
            self.url = self.url.replace('&quot', '')

        if self.url.startswith('..'):
            self.url = self.url[2:]

        if self.url.startswith('/..'):
            print(self.url)
            self.url = self.url[3:]

        if (self.url.startswith('/') and not self.url.startswith('//')) or self.url.startswith('\\'):
            self.url = self.url[1:]

    def get_domain(self):
        return parse.urlparse(self.url).netloc