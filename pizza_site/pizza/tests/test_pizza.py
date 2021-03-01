from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from pizza.models import Topping, Size, Pizza
from pizza.serializers import SizeSerializer, ToppingSerializer, PizzaSerializer, PizzaDetailSerializer


SIZE_URL = reverse('pizza:size-list')
TOPPING_URL = reverse('pizza:topping-list')
PIZZA_URL = reverse('pizza:pizza-list')


def detail_url(pizza_id):
    """ find the pizza with its id"""
    return reverse('pizza:pizza-detail', args=[pizza_id])


class PizzaApiTests(TestCase):
    """ • Size API testing
        • Topping API testing
        • Pizza API testing
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

    def test_fetching_a_list_of_sizes(self):
        """In this test we test that we get a list of sizes in response"""
        # add sizes to the test DB
        Size.objects.create(name="Mediumish Large")
        Size.objects.create(name="Smallishsss Medium")
        # the SIZE_URL will call the router which would invoke the list function
        res = self.client.get(SIZE_URL)
        # We will call the objects serialize them and compare with our request
        sizes = Size.objects.all().order_by('name')
        serializer = SizeSerializer(sizes, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

        self.assertEquals(res.data, serializer.data)

    def test_create_valid_topping_success(self):
        """Since we have create the Topping(Pizza-Topping) model with 
            the dunder method of string(__str__).
            It will return the string representation of the 
            "name" attribute.
            We will check if that is same as what we have set.
        """
        topping = Topping.objects.create(name="Pepperoni")

        self.assertEquals(str(topping), topping.name)

    def test_fetching_a_list_of_toppings(self):
        """Fetching
        """
        # add new toppings to the test DB
        Topping.objects.create(name="Mushrooms")
        Topping.objects.create(name="Baby Corn")
        # the URL will call the router which would invoke the list function
        res = self.client.get(reverse('pizza:topping-list'))
        # We will call the objects, serialize them and compare with our request
        toppings = Topping.objects.all().order_by('name')
        serializer = SizeSerializer(toppings, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

        self.assertEquals(res.data, serializer.data)

    def test_for_invalid_size_and_topping(self):
        payload = {"name": ""}
        # for size
        res = self.client.post(SIZE_URL, payload)
        self.assertEquals(res.status_code, status.HTTP_400_BAD_REQUEST)
        # for topping
        res = self.client.post(TOPPING_URL, payload)
        self.assertEquals(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_pizzas(self):
        #Size is Large
        pizza_size_val = Size.objects.get_or_create(name="LARGE")
        topping1 = Topping.objects.get_or_create(name="Tomato")
        topping2 = Topping.objects.get_or_create(name="Corn")
        topping3 = Topping.objects.get_or_create(name="Jalapeno")
        Pizza.objects.create(
            name='Pasta Pizza',
            pizza_shape="SQUARE",
            pizza_size=pizza_size_val.id,
            pizza_topping=[topping1.id, topping2.id, topping3.id]
        )
        res = self.client.get(PIZZA_URL)

        pizzas = Pizza.objects.all()
        serializer = PizzaSerializer(pizzas, many=True)

        self.assertEquals(res.status_code, status.HTTP_200_OK)
        self.assertEquals(res.data, serializer.data)

    # def test_view_pizza_detail(self):
    #     pizza = Pizza.objects.create(
    #         name='Pasta Pizza',
    #         pizza_shape="SQUARE",
    #         pizza_size=3,
    #         pizza_topping=["Tomato", "Corn", "Jalapeno"]
    #     )
    #     url = detail_url(pizza.id)
    #     res = self.client.get(url)

    #     serializer = PizzaDetailSerializer(pizza)
    #     self.assertEquals(res.data, serializer.data)
