from django.test import TestCase
from .models import Snippet
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# Create your tests here.


class SnippetTestCase(APITestCase):

    def setUp(self):
        self.test_snippet = Snippet.objects.create(title='test1', code='code1')
        self.user = User.objects.create_user(username='test', email='test@gmail.com', password='abc@12345')
        self.token = self.client.post('/api-token-auth/',
                                      data={'username': 'test', 'password': 'abc@12345'}).json()['token']

    def tearDown(self):
        Snippet.objects.all().delete()
        User.objects.all().delete()
        Token.objects.all().delete()

    def test_get_snippet(self):
        assert str(self.test_snippet) == 'test1'
        response = self.client.get('/snippets/', format='json')
        assert response.status_code == 200

    def test_post_unauthentication(self):
        data = {
            'title': 'test2',
            'code': 'code2'
        }
        response = self.client.post('/snippets/', data=data, format='json')
        assert response.status_code == 401

    def test_post_snippet(self):
        data = {
            'title': 'test2',
            'code': 'code2'
        }
        response = self.client.post('/snippets/', data=data, format='json', HTTP_AUTHORIZATION='Token ' + self.token)
        print(response.json())
        assert response.status_code == status.HTTP_201_CREATED
        data_response = response.json()

    def test_post_invalid_unique(self):
        data = {
            'title': 'test1',
            'code': 'code2'
        }
        response = self.client.post('/snippets/', data=data, format='json', HTTP_AUTHORIZATION='Token ' + self.token)
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_post_invalid(self):
        data = {
            'title': 'error',
            'code': 'code2'
        }
        response = self.client.post('/snippets/', data=data, format='json', HTTP_AUTHORIZATION='Token ' + self.token)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        print(response.json())

    def test_post_blank(self):
        data = {
            'title': '',
            'code': ''
        }
        response = self.client.post('/snippets/', data=data, format='json', HTTP_AUTHORIZATION='Token ' + self.token)
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_get_detail(self):
        response = self.client.get('/snippets/{}/'.format(self.test_snippet.id), format='json')
        assert response.status_code == 200

    def test_put_details(self):
        data = {
            'code': 'put code2'
        }
        response = self.client.put('/snippets/{}/'.format(self.test_snippet.id), data=data, format='json')
        assert response.status_code == 200
        data_response = response.json()
        assert data_response['code'] == 'put code2'

    def test_delete(self):
        response = self.client.delete('/snippets/{}/'.format(self.test_snippet.id), format='json')
        assert response.status_code == status.HTTP_204_NO_CONTENT
