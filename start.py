import sys
import time

from multiprocessing.pool import ThreadPool as Pool

from main import Main

MAX_POOL_SIZE = 5
COMMAND_LINE_ARGUMENTS = {
    'CRAWL': ['--crawl', '-c'],
    'FILE': '--file'
}


def start():
    input_file = get_input_file()
    should_crawl = is_crawl_request()

    if input_file:
        return process_file(input_file, should_crawl)

def is_crawl_request():

    args = sys.argv
    
    for argument in COMMAND_LINE_ARGUMENTS['CRAWL']:
        if argument in args:
            return True

    return False

def get_input_file():

    try:

        args = sys.argv
        index = args.index(COMMAND_LINE_ARGUMENTS['FILE'])

        if index and len(args) > index + 1:
            return args[index + 1]

        return None

    except Exception as e:
        return None

def process_file(filename, is_crawl_request):

    fyle = open(filename, 'r')
    file_lines = fyle.readlines()

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
