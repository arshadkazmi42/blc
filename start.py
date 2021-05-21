import sys

from main import Main


def get_args():

    args = sys.argv

    if len(args) < 2:
        print('You should pass the URL to the script in command line parameter')
        print('Eg: python start.py [YOUR_URL]')
        exit()

    return args[1]


url = get_args()
main = Main(url)
main.run()