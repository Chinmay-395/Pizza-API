from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from pizza.models import Topping, Size


class SizeApiTests(TestCase):
    """Size API testing

    """

    def test_create_valid_size_success(self):
        """Since we have create the Size(Pizza-Size) model with 
            the dunder method of string(__str__).
            It will return the string representation of the 
            "name" attribute.
            We will check if that is same as what we have set.
        """
        size = Size.objects.create(name="Mediumish_Large")

        self.assertEquals(str(size), size.name)
