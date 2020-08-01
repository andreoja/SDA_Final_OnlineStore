from django.contrib import admin
from .models import Product, Dimension, Weight

admin.site.register(Product)
admin.site.register(Dimension)
admin.site.register(Weight)