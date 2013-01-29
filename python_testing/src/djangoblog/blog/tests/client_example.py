import unittest2
from django.test.client import Client

class SimpleTest(unittest2.TestCase):
    #fixtrues = ['manyposts.json']

    def setUp(self):
        self.client = Client()

    def test_details(self):
        # Issue a GET request.
        response = self.client.get('/blog/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Look for known string in content.
        self.assertRegexpMatches(response.content, "Headline")

        # Check that the rendered context contains 5 customers.
        self.assertEqual(len(response.context['latest']), 1)
