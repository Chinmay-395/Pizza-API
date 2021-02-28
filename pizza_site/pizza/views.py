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


class BasePizzaAttributeViewSet(
        viewsets.GenericViewSet,
        mixins.ListModelMixin,
        mixins.CreateModelMixin):
    """Base viewset for user owned pizza attributes """

    def get_queryset(self):
        return self.queryset.order_by('name')

    def perform_create(self, serializer):
        """Create a new object"""
        return serializer.save()


class ToppingModelViewSet(BasePizzaAttributeViewSet):
    """Manage Toppings of Pizza in the DB"""
    # ordered by name because it would easier to browse
    queryset = Topping.objects.all().order_by('name')
    serializer_class = ToppingSerializer


class SizeModelViewSet(BasePizzaAttributeViewSet):
    """Manage Sizes of Pizza in the DB"""
    # ordered by name because it would easier to browse
    queryset = Size.objects.all().order_by('name')
    serializer_class = SizeSerializer
