import mimetypes

from urllib import parse


MIME_TYPES_MEDIA = ['audio', 'video', 'image', 'font', 'application/zip', 'application/x-debian-package', 'application/pdf', 'application/x-redhat-package-manager', 'application/x-apple-diskimage', 'application/x-msdos-program', 'application/x-tar']


class Link:
    
    def __init__(self, url):
        self.url = url

        self.clean()
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

    def is_same_domain(self, url):

        domain = parse.urlparse(url).netloc
        
        if self.domain in domain:
            return True
        
        if len(domain) != len(self.domain):
            return False

        index = len(domain) - 1
        while(index > 0):
            if domain[i] != self.domain[i]:
                return False

        return True

    def is_media_url(self, url):
        
        url_path = parse.urlparse(url).path
        mimetype,encoding = mimetypes.guess_type(url_path)
        if mimetype and (mimetype.startswith(tuple(MIME_TYPES_MEDIA))):
            return True

        return False