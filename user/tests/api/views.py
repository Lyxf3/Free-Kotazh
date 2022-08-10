# region				-----External Imports-----
from rest_framework.test import APITestCase, URLPatternsTestCase
from rest_framework import (status as rest_status)
from django.urls import include, path, reverse
# endregion

# region				-----Internal Imports-----
from ... import models as user_models
# endregion

# region			  -----Supporting Variables-----
# endregion


class UserTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('api/', include('user.urls')),
    ]
    response_keys = ["id", "username", "image", "phone", "second_name",
                     "first_name", "bio", "phone_verified", "is_online"]

    def test_create(self):
        url = "frontend/user/"
        data = {"username": "test", "phone": "+380500000000"}
        response = self.client.post(data=data, path=url, format='json')
        self.assertEqual(response.status_code, rest_status.HTTP_201_CREATED)
        self.assertEqual(list(response.data.keys()), self.response_keys)

    def test_retrieve(self):
        url = "frontend/user/1/"
        self.client.login(username="admin", password="admin")
        response = self.client.get(path=url, format='json')
        self.assertEqual(response.status_code, rest_status.HTTP_200_OK)
        self.assertEqual(list(response.data.keys()), self.response_keys)
        self.client.logout()

    def test_partial_update(self):
        url = "frontend/user/1/"
        self.client.login(username="admin", password="admin")
        data = {"first_name": "test123"}
        response = self.client.patch(data=data, path=url, format='json')
        self.assertEqual(response.status_code, rest_status.HTTP_200_OK)
        self.assertEqual(list(response.data.keys()), self.response_keys)
        self.client.logout()


class DungeonBookTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('api/', include('user.urls')),
    ]
    response_keys = ["id", "slave"]

    def test_create(self):
        url = "frontend/dungeon/book/"
        user_models.User.objects.create(username="test", phone="+380500000001")
        data = {"slave": "test"}
        response = self.client.post(data=data, path=url, format='json')
        self.assertEqual(response.status_code, rest_status.HTTP_201_CREATED)
        self.assertEqual(list(response.data.keys()), self.response_keys)

    def test_list(self):
        url = "frontend/dungeon/book/"
        self.client.login(username="admin", password="admin")
        response = self.client.get(path=url, format='json')
        self.assertEqual(response.status_code, rest_status.HTTP_200_OK)
        self.assertEqual(list(response.data.keys()), self.response_keys)
        self.client.logout()
