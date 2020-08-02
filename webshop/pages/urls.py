from django.urls import path
from pages.views import ProductListView, CreateProductView, UpdateProductView
from pages.views import DeleteProductView, DetailProductView, ContactView


urlpatterns = [
    path('list/', ProductListView.as_view(), name='list'),
    path('create/', CreateProductView.as_view(), name='create'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('detail/<int:pk>', DetailProductView.as_view(), name='detail'),
    path('update/<int:pk>', UpdateProductView.as_view(), name='update'),
    path('delete/<int:pk>', DeleteProductView.as_view(), name='delete')
]