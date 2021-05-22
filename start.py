import sys
import time

from main import Main


def start():
    url = get_args()
    main = Main(url)
    main.run()

def get_args():

    args = sys.argv

    if len(args) < 2:
        print('You should pass the URL to the script in command line parameter')
        print('Eg: python start.py [YOUR_URL]')
        exit()

    return args[1]


start_time = time.time()
start()
print("Processed in %s minutes" % ((time.time() - start_time) / 60))