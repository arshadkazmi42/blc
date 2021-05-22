import sys
import time

from main import Main


CRAWL_ARGUMENT = ['--crawl', '-c']


def start():
    url = get_args()
    main = Main(url, is_crawl_request())
    main.run()

def get_args():

    args = sys.argv

    if len(args) < 2:
        print('You should pass the URL to the script in command line parameter')
        print('Eg: python start.py [YOUR_URL]')
        exit()

    return args[1]

def is_crawl_request():

    args = sys.argv
    
    for carg in CRAWL_ARGUMENT:
        if carg in args:
            return True

    return False


start_time = time.time()
start()
print("Processed in %s minutes" % ((time.time() - start_time) / 60))