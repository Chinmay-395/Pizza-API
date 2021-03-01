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
    # pizza_size = SizeSerializer(read_only=True)
    pizza_topping = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Topping.objects.all()
    )

    class Meta:
        model = Pizza
        fields = [
            'id',
            'name',
            'pizza_shape',
            'pizza_size',
            'pizza_topping',
        ]
        read_only_fields = ['id']


class PizzaDetailSerializer(PizzaSerializer):
    """Serialize a pizza details"""
    pizza_size = SizeSerializer(read_only=True)
    pizza_topping = ToppingSerializer(many=True, read_only=True)
