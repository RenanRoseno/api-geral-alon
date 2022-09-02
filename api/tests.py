from django.test import TestCase
from django.urls import reverse, resolve
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory, APIClient
from django.test import SimpleTestCase

from api.viewsets.campusViewSet import CampusViewSet
from api.viewsets.cityViewSet import CityViewSet


class TestsAPI(APITestCase):

    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """

        url = reverse('campus-list')
        print(url)
        #response = self.client.post(url, format='json')


