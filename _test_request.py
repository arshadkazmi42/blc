import unittest
from unittest.mock import Mock, patch

from request import Request


RESPONSE = {
    "status": "success",
    "message": "Processed"
}

class Response:

    def __init__(self):
        self.text = RESPONSE['message']

    def json(self):
        return RESPONSE


mock_response = Response()


class TestRequest(unittest.TestCase):

    def test_init(self):

        request = Request()

        self.assertNotEqual(request.headers, None, f'Should not be None')
        self.assertNotEqual(request.timeout, None, f'Should not be None')

    @patch('request.requests.head')
    def test_head(self, mock_head):

        URL = 'https://example.com/working'

        mock_head.return_value.status_code = 200

        request = Request()

        self.assertEqual(request.head(URL).status_code, 200, f'Should return 200 status code')

    @patch('request.requests.head')
    def test_status_code_400(self, mock_head):

        URL = 'https://example.com/not_found'

        mock_head.return_value.status_code = 400

        request = Request()

        self.assertEqual(request.get_status_code(URL), 400, f'Should return 400 status code')

    @patch('request.requests.get')
    def test_get(self, mock_get):

        URL = 'https://example.com/working'
        
        mock_get.return_value = mock_response

        request = Request()
        response = request.get(URL)
        response = response.json()

        self.assertEqual(response['status'], RESPONSE['status'], f'Should return success status')
        self.assertEqual(response['message'], RESPONSE['message'], f'Should return Processed message')

    @patch('request.requests.get')
    def test_get_text_response(self, mock_post):

        URL = 'https://example.com/working'

        mock_post.return_value = mock_response

        request = Request()
        response = request.get_text_response(URL)

        self.assertEqual(response, RESPONSE['message'], f'Should {RESPONSE["message"]} message')

    @patch('request.requests.get')
    def test_get_json_response(self, mock_post):

        URL = 'https://example.com/working'

        mock_post.return_value = mock_response

        request = Request()
        response = request.get_json_response(URL)

        self.assertEqual(response['status'], RESPONSE['status'], f'Should return success status')
        self.assertEqual(response['message'], RESPONSE['message'], f'Should return Processed message')

if __name__ == '__main__':
    unittest.main()