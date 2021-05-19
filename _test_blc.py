import unittest
from unittest.mock import Mock, patch

from link import Link
from blc import BrokenLinkChecker


class TestBrokenLinkChecker(unittest.TestCase):

    def test_init(self):
        URL = 'https://hackerone.com/login?xyz=123'
        lnk = Link(URL)

        blc = BrokenLinkChecker(lnk)

        self.assertEqual(blc.link.url, URL, f'Should return the original url')

    @patch('blc.requests.head')
    def test_broken_link(self, mock_head):

        mock_head.return_value.status_code = 404

        URL = 'https://example.com/broken'
        lnk = Link(URL)

        blc = BrokenLinkChecker(lnk)

        self.assertEqual(blc.is_broken(), True, f'Should return True for valid url')

    @patch('blc.requests.head')
    def test_broken_link(self, mock_head):

        mock_head.return_value.status_code = 200

        URL = 'https://example.com/working'
        lnk = Link(URL)

        blc = BrokenLinkChecker(lnk)

        self.assertEqual(blc.is_broken(), False, f'Should return True for valid url')

if __name__ == '__main__':
    unittest.main()