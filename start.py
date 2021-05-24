import sys
import time

from multiprocessing.pool import ThreadPool as Pool

from main import Main

MAX_POOL_SIZE = 10
COMMAND_LINE_ARGUMENTS = {
    'CRAWL': '--crawl',
    'FILE': '--file'
}


def start():
    input_file = get_input_file()
    crawl_file = get_crawl_file()

    if input_file:
        return process_file(input_file)

    if crawl_file:
        should_crawl = True
        return process_file(crawl_file, should_crawl)

def get_crawl_file():
    return get_file(COMMAND_LINE_ARGUMENTS['CRAWL'])


def get_input_file():
    return get_file(COMMAND_LINE_ARGUMENTS['FILE'])

def get_file(cmd_argument):

    try:

        args = sys.argv
        index = args.index(cmd_argument)

        if index and len(args) > index + 1:
            return args[index + 1]

        return None

    except Exception as e:
        return None

def process_file(filename, is_crawl_request=False):

    fyle = open(filename, 'r')
    file_lines = fyle.read().splitlines()

    pool = Pool(MAX_POOL_SIZE)

    for line in file_lines:
        pool.apply_async(process_url, (line,is_crawl_request,))

    pool.daemon = True
    pool.close()
    pool.join()

def process_url(url, is_crawl_request=None):
    main = Main(url, is_crawl_request)
    main.run()


start_time = time.time()
start()
print("Processed in %s minutes" % ((time.time() - start_time) / 60))
