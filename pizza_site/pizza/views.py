from rest_framework import mixins, viewsets
from django.shortcuts import get_object_or_404
from .serializers import PizzaSerializer, SizeSerializer, ToppingSerializer, PizzaDetailSerializer
from .models import Pizza, Size, Topping


class PizzaModelViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

    def perform_create(self, serializer):
        print("THE SELF ACTION ===>", self.action)
        return super().perform_create(serializer)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return PizzaDetailSerializer

        if self.action == "list":
            return PizzaSerializer


class ToppingModelViewSet(
        viewsets.GenericViewSet,
        mixins.ListModelMixin,
        mixins.CreateModelMixin):
    """Manage Toppings of Pizza in the DB"""
    # ordered by name because it would easier to browse
    queryset = Topping.objects.all().order_by('name')
    serializer_class = ToppingSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)


class SizeModelViewSet(
        viewsets.GenericViewSet,
        mixins.ListModelMixin,
        mixins.CreateModelMixin):
    """Manage Sizes of Pizza in the DB"""
    # ordered by name because it would easier to browse
    queryset = Size.objects.all().order_by('name')
    serializer_class = SizeSerializer

    def perform_create(self, serializer):
        """Create a new size"""
        return super().perform_create(serializer)
