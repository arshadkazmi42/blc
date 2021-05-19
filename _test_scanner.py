import unittest

from scanner import Scanner


class TestRequest(unittest.TestCase):

    def test_init(self):

        scanner = Scanner()

        self.assertNotEqual(scanner.regex_link, None, f'Should not be None')

    def test_matches(self):

        text = 'Something here https://hackerone.com url is here'
        scanner = Scanner()
        matches = scanner.find_all_links(text)
        
        self.assertEqual(len(matches), 1, 'Should be of length 1')
        self.assertEqual(matches[0], 'https://hackerone.com', 'Should have correct URL')

if __name__ == '__main__':
    unittest.main()