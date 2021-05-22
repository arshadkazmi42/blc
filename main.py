from multiprocessing.pool import ThreadPool as Pool

from blc import BrokenLinkChecker
from file_operations import FileOperations
from link import Link
from request import Request
from scanner import Scanner


MAX_POOL_SIZE = 10


class Main:

    def __init__(self, url, is_crawl_request=False):

        self.should_crawl = is_crawl_request

        self.link = Link(url)
        self.blc = BrokenLinkChecker()
        self.file_operations = FileOperations(self.link)
        self.request = Request()
        self.scanner = Scanner()

        self.pool_size = MAX_POOL_SIZE

        print_line = f'Processing {url}'
        print(print_line)

        self.file_operations.write_in_output(print_line)

    def run(self):

        url = self.link.get_url()

        try:
            
            response = self.request.get_text_response(url)
            if not response:
                return None

            self.parse_response(response)

        except Exception as e:
            print(f'Error processing url {url}')
            print(e)

    def parse_response(self, response):

        pool = Pool(self.pool_size)
        matches = self.scanner.find_all_links(response)
        for url in matches:
            pool.apply_async(self.process, (url,))

        pool.daemon = True
        pool.close()
        pool.join()

    def process(self, url):

        if self.should_crawl:
            self.process_crawl(url)    
        else:    
            self.process_blc(url)


    def process_blc(self, url):

        self.file_operations.write_in_output(url)

        if self.link.is_same_domain(url):
            return None

        if not self.blc.is_broken(url):
            print_line = f'|---OK---| {url}'
            print(print_line)
            return None

        print_line = f'|-BROKEN-| {url}'
        print(print_line)

        self.file_operations.write_in_broken(url)

    def process_crawl(self, url):

        is_mime_url = self.link.is_mime_url(url)
        is_same_domain_url = self.link.is_same_domain(url)

        if is_same_domain_url and not is_mime_url:

            print(f'Found link: {url}')
            self.file_operations.write_in_links(url)