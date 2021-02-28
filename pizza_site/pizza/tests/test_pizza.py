from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from pizza.models import Topping, Size


class SizeApiTests(TestCase):
    """Size API testing

    """

    def test_create_valid_size_success(self):
        size = Size.objects.create(name="Mediumish_Large")

        self.assertEquals(str(size), size.name)
