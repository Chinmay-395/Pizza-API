from django.contrib import admin
from .models import Pizza, Size, Topping
# Register your models here.


class PizzaAdmin(admin.ModelAdmin):
    fields = ['name', 'pizza_size', 'pizza_shape']
    ordering = ['id']
    list_display = ['name', 'pizza_size', 'pizza_shape']


admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Size)
admin.site.register(Topping)
