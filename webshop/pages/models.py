from django.db import models


class Dimension(models.Model):
    l = models.FloatField(default=0.0)
    h = models.FloatField(default=0.0)
    w = models.FloatField(default=0.0)


    def __str__(self):
        return 'L=' + str(self.l) + ',' + 'H=' + str(self.h) + ',' + 'W=' + str(self.w)


class Weight(models.Model):
    kg = models.FloatField(default=0.0)

    def __str__(self):
        return 'Weight=' + str(self.kg) + 'Kg'


class Product(models.Model):
    part_number = models.CharField(max_length=15)
    car_brand = models.CharField(max_length=30)
    ean_code = models.CharField(max_length=20)
    product_name_EN = models.CharField(max_length=40)
    product_name_EE = models.CharField(max_length=40)
    product_info = models.TextField(null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0)
    warehouse_address = models.CharField(max_length=10)
    location_address = models.CharField(max_length=8)
    price = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True)

    dimensions = models.CharField(max_length=30, null=True, blank=True)
    weight = models.DecimalField(
        max_digits=9, decimal_places=3, null=True, blank=True)

    def __str__(self):
        return self.name
