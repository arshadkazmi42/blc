import unittest
from unittest.mock import Mock, patch

from blc import BrokenLinkChecker


class TestBrokenLinkChecker(unittest.TestCase):

    def test_init(self):

        blc = BrokenLinkChecker()

        self.assertNotEqual(blc.request, None, f'Should have request object')

    @patch('request.requests.head')
    def test_broken_link(self, mock_head):

        mock_head.return_value.status_code = 404

        blc = BrokenLinkChecker()

        self.assertEqual(blc.is_broken('https://example.com/broken'), True, f'Should return True for valid url')

    @patch('request.requests.head')
    def test_broken_link(self, mock_head):

        mock_head.return_value.status_code = 200

        blc = BrokenLinkChecker()

        self.assertEqual(blc.is_broken('https://example.com/working'), False, f'Should return True for valid url')

if __name__ == '__main__':
    unittest.main()