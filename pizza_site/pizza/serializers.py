from rest_framework import serializers

from .models import Pizza, Size, Topping


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['id', 'name']
        read_only_fields = ['id']


class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = ['id', 'name']
        read_only_fields = ['id']


class PizzaSerializer(serializers.ModelSerializer):
    pizza_sizes = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Size.objects.all()
    )
    pizza_toppings = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Topping.objects.all()
    )

    class Meta:
        model = Pizza
        fields = [
            'id',
            'pizza_shape',
            'pizza_sizes',
            'pizza_toppings',
        ]
        read_only_fields = ['id']


class PizzaDetailSerializer(PizzaSerializer):
    pizza_sizes = SizeSerializer(many=True, read_only=True)
    pizza_toppings = ToppingSerializer(many=True, read_only=True)
