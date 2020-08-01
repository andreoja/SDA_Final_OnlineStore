from rest_framework import serializers
from pages.models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['part_number', 'product_name_EE', 'price', 'weight']

