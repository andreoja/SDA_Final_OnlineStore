from django.contrib import admin
from pages.models import Product, CategoryPart, CategoryCarBrand, StoreUser, Cart, CartItem

admin.site.register(Product)
admin.site.register(StoreUser)
admin.site.register(CategoryPart)
admin.site.register(CategoryCarBrand)
admin.site.register(Cart)
admin.site.register(CartItem)
