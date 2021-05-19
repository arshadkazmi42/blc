import unittest
from unittest.mock import patch, mock_open

from link import Link
from file_operations import FileOperations

## TODO Figure out a way to test file read and write

class TestBrokenLinkChecker(unittest.TestCase):

    def test_init(self):
        URL = 'https://hackerone.com/login?xyz=123'
        lnk = Link(URL)

        file_operations = FileOperations(lnk)

        self.assertEqual(file_operations.broken_file_name, 'broken.txt', f'Should return broken.txt as filename')
        self.assertEqual(file_operations.output_file_name, 'output.txt', f'Should return output.txt as filename')

    def test_create_file_operations_directory_name(self):
        URL = 'https://hackerone.com/login?xyz=123'
        lnk = Link(URL)

        file_operations = FileOperations(lnk)

        self.assertEqual(file_operations.directory_name, 'hackerone.com', f'Should return hackerone.com as directory name')

if __name__ == '__main__':
    unittest.main()