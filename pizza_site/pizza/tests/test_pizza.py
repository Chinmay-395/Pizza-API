from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status


class SizeApiTests(TestCase):
    """Size API

    Args:
        TestCase ([type]): [description]
    """

    def test_create_valid_size_success(self):
        payload = {
            "name": "Mediumish_Large"
        }
        res = self.client.post(
            reverse('pizza:create'),
            payload
        )

        self.assertEquals(res.status_code, status.HTTP_201_CREATED)
