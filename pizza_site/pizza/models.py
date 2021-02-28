from django.db import models


class Size(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Topping(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Create your models here.


class Pizza(models.Model):
    """Pizza object"""
    REGULAR = "REGULAR"
    SQUARE = "SQUARE"
    TYPE_CHOICE = (
        (REGULAR, REGULAR),
        (SQUARE, SQUARE)
    )
    name = models.CharField(max_length=255, default="**No-Name**")
    pizza_shape = models.CharField(
        max_length=200, choices=TYPE_CHOICE, default=REGULAR)
    pizza_size = models.ForeignKey(Size, on_delete=models.CASCADE)
    pizza_topping = models.ManyToManyField('Topping')

    def __str__(self):
        return f'{self.name}'
