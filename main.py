from blc import BrokenLinkChecker
from file_operations import FileOperations
from link import Link


def run(url):

    link = Link(url)

    blc = BrokenLinkChecker(link)
    file_operations = FileOperations(link)

    # Write all urls in output
    file_operations.write_in_output(link.url)

    if blc.is_broken():
        file_operations.write_in_broken(link.url)
        