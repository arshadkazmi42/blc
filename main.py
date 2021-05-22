from multiprocessing.pool import ThreadPool as Pool

from blc import BrokenLinkChecker
from file_operations import FileOperations
from link import Link
from request import Request
from scanner import Scanner


class Main:

    def __init__(self, url):

        self.pool_size = 10

        self.link = Link(url)
        self.blc = BrokenLinkChecker()
        self.file_operations = FileOperations(self.link)
        self.request = Request()
        self.scanner = Scanner()

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
        