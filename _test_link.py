import unittest

from link import Link


class TestLink(unittest.TestCase):

    def test_link_create(self):
        URL = 'https://hackerone.com/login?xyz=123'
        lnk = Link(URL)
        self.assertEqual(lnk.url, URL, f'Should return the original url')

    def test_link_clean_ending_dot(self):
        
        URL = 'https://hackerone.com/login.'
        CLEAN_URL = 'https://hackerone.com/login'

        lnk = Link(URL)
        lnk.clean()

        self.assertEqual(lnk.url, CLEAN_URL, f'Should return the url without (.) removed')

    def test_link_clean_ending_quote(self):
        
        URL = 'https://hackerone.com/login"'
        CLEAN_URL = 'https://hackerone.com/login'

        lnk = Link(URL)
        lnk.clean()

        self.assertEqual(lnk.url, CLEAN_URL, f'Should return the url without (") removed')

    def test_link_clean_ending_single_quote(self):
        
        URL = 'https://hackerone.com/login\''
        CLEAN_URL = 'https://hackerone.com/login'

        lnk = Link(URL)
        lnk.clean()

        self.assertEqual(lnk.url, CLEAN_URL, f'Should return the url without (\') removed')

    def test_link_clean_ending_single_quote(self):
        
        URL = 'https://hackerone.com/login\''
        CLEAN_URL = 'https://hackerone.com/login'

        lnk = Link(URL)
        lnk.clean()

        self.assertEqual(lnk.url, CLEAN_URL, f'Should return the url without (\') removed')

    def test_link_clean_ending_quote_text(self):
        
        URL = 'https://hackerone.com/login&quot'
        CLEAN_URL = 'https://hackerone.com/login'

        lnk = Link(URL)
        lnk.clean()

        self.assertEqual(lnk.url, CLEAN_URL, f'Should return the url without (&quot) removed')

    def test_link_clean_ending_slash(self):
        
        URL = '\\https://hackerone.com/login'
        CLEAN_URL = 'https://hackerone.com/login'

        lnk = Link(URL)
        lnk.clean()

        self.assertEqual(lnk.url, CLEAN_URL, f'Should return the url without (\\) removed')

    def test_link_clean_ending_double_dot(self):
        
        URL = '..https://hackerone.com/login'
        CLEAN_URL = 'https://hackerone.com/login'

        lnk = Link(URL)
        lnk.clean()

        self.assertEqual(lnk.url, CLEAN_URL, f'Should return the url without (..) removed')
    
    def test_link_clean_ending_slash_double_dot(self):
        
        URL = '/..hackerone.com/login'
        CLEAN_URL = 'hackerone.com/login'

        lnk = Link(URL)
        lnk.clean()

        self.assertEqual(lnk.url, CLEAN_URL, f'Should return the url without (..) removed')

    def test_get_url_domain(self):
        
        URL = 'https://sub.hackerone.com/login'
        DOMAIN = 'sub.hackerone.com'

        lnk = Link(URL)

        self.assertEqual(lnk.get_domain(), DOMAIN, f'Should return the domain of the url {DOMAIN}')

if __name__ == '__main__':
    unittest.main()