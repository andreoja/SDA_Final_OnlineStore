from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib import admin
from pages.views import ProductListView, CreateProductView, UpdateProductView
from pages.views import DeleteProductView, DetailProductView, ContactView, CartView, cart_add
from pages.views import PurchaseSuccessView, purchase_view, register_user


urlpatterns = [
    path('cart_add/<int:product_id>/', cart_add, name='cart_add'),
    path('list/', ProductListView.as_view(), name='list'),
    path('create/', CreateProductView.as_view(), name='create'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('cart/', CartView.as_view(), name='cart'),
    path('detail/<int:pk>', DetailProductView.as_view(), name='detail'),
    path('update/<int:pk>', UpdateProductView.as_view(), name='update'),
    path('delete/<int:pk>', DeleteProductView.as_view(), name='delete'),
    path('cart/', CartView.as_view(), name='cart'),
    path('purchase/', purchase_view, name='purchase'),
    path('purchase_success/', PurchaseSuccessView.as_view(), name='purchase_success'),
]