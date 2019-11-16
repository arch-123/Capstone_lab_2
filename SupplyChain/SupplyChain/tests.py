from django.test import TestCase

# Create your tests here.
from django.http import HttpRequest
from django.urls import reverse

class HomePageTests(TestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)