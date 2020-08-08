from django.db import models


class CategoryPart(models.Model):
    class Meta:
        verbose_name_plural = "categories"

    name = models.CharField(max_length=20)
    perishable = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ' - prerishable:' + str(self.perishable)

class CategoryCarBrand(models.Model):
    class Meta:
        verbose_name_plural = "categories"

    name = models.CharField(max_length=15)
    perishable = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ' - prerishable:' + str(self.perishable)


class Product(models.Model):
    part_number = models.CharField(max_length=15)
    category_car_brand = models.ForeignKey(
        CategoryCarBrand, on_delete=models.DO_NOTHING, null=True, blank=True)
    ean_code = models.CharField(max_length=20)
    product_name_EN = models.CharField(max_length=40)
    product_name_EE = models.CharField(max_length=40)
    category_part = models.ForeignKey(
        CategoryPart, on_delete=models.DO_NOTHING, null=True, blank=True)
    product_info = models.TextField(null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0)
    warehouse_address = models.CharField(max_length=10)
    location_address = models.CharField(max_length=8)
    price = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True)
    dimensions = models.CharField(max_length=30, null=True, blank=True)
    weight = models.DecimalField(
        max_digits=9, decimal_places=3, null=True, blank=True)
    picture = models.ImageField(upload_to='images/', null=True, blank=True)
    front_img = models.ImageField(upload_to='images/', null=True, blank=True)
    back_img = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.part_number
