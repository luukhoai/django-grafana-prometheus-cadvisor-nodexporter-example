from django.test import TestCase

# Create your tests here.

from json import dumps, loads
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
# Create your tests here.
import logging
logger = logging.getLogger('test_django')


class AccountTests(TestCase):

    def setUp(self):
        self.username = 'test'
        self.email = 'test@gmail.com'
        self.password = 'test@12345'

    def test_login_account(self):
        user = User.objects.create_user(username=self.username, email=self.email, password=self.password)
        data = {
            'username': self.username,
            'password': self.password,
        }
        response = self.client.post('/accounts/login', data, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        data_response = loads((response.content.decode('utf-8')))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data_response['success'], True)

    def test_login_incorrect(self):
        data = {
            'username': self.username,
            'password': self.password,
        }
        response = self.client.post('/accounts/login', data, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        data_response = loads((response.content.decode('utf-8')))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data_response['success'], False)

    def test_clean_user_or_password(self):
        data = {
            'username': '',
            'password': self.password,
        }
        response = self.client.post('/accounts/login', data, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        data_response = loads((response.content.decode('utf-8')))
        print(data_response)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data_response['success'], False)


    def test_password_too_short(self):
        data = {
            'username': self.username,
            'password': '123',
        }
        response = self.client.post('/accounts/login', data, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        data_response = loads((response.content.decode('utf-8')))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data_response['success'], False)
