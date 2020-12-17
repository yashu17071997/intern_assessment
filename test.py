"""
to create a test project for simple api in flask
"""
import unittest
import requests


class TestApi(unittest.TestCase):
    """Test to send payload input and validate the responses accordingly """
    api_url = "http://localhost:5000/v1/sanitized/input"

    def test_sanitized_returns_ok(self):
        """Test to send sanitized input and validate the response"""
        headers = {'Content-type': 'application/json'}

        response = requests.post(TestApi.api_url, json={"payload": "7865thg"}, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'{\n    "result": "sanitized"\n}\n')

    def test_un_sanitized_returns_ok(self):
        """Test to send unsanitized input and validate the response """
        headers = {'Content-type': 'application/json'}

        response = requests.post(TestApi.api_url,
                                 json={"payload": "Delete where Id='1'"},
                                 headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'{\n    "result": "unsanitized"\n}\n')

    def test_returns_bad_request(self):
        """Test to validate the response is 400 or not"""
        headers = {'Content-type': 'application/json'}

        response = requests.post(TestApi.api_url, json={"payload": ""}, headers=headers)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, b'"bad request!"\n')
