from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (PizzaModelViewSet,
                    ToppingModelViewSet,
                    SizeModelViewSet)


router = DefaultRouter()
router.register('pizza', PizzaModelViewSet)
router.register('topping', ToppingModelViewSet)
router.register('size', SizeModelViewSet)

app_name = 'pizza'

urlpatterns = [
    path('', include(router.urls))
]
