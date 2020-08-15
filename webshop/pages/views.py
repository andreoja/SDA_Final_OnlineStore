from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView, FormView
from pages.models import Product, Cart, CartItem
from pages.forms import ContactForm
from django.urls import reverse_lazy
import random
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from rest_framework import viewsets
from pages.serializers import ProductSerializer


def cart_add(request, product_id):
    user = request.user
    carts = Cart.objects.filter(user=user).filter(active=True)
    user_cart = None

    if carts.count() ==0:
        new_cart = Cart.objects.create(user=user)
        new_cart.save()
        user_cart = new_cart

    else:
        user_cart = carts.first()

    product = Product.objects.filter(id=product_id).first()
    cart_items = user_cart.cartitems.filter(product=product)

    if cart_items.count() == 0:
        new_cartitem = CartItem.objects.create(product=product)
        new_cartitem.save()
        user_cart.cartitems.add(new_cartitem)
    else:
        cart_item = cart_items.first()
        cart_item.quantity = cart_item.quantity + 1
        cart_item.save()

    return HttpResponseRedirect(reverse_lazy('cart'))

class ProductListView(ListView):
    model = Product
    template_name = 'list.html'
    context_object_name = 'products'

    def get_queryset(self):
        filter_val = self.request.GET.get('filter', None)
        order = self.request.GET.get('orderby', 'part_number')

        new_queryset = Product.objects.order_by(order)

        if filter_val:
            new_queryset = new_queryset.filter(part_number__icontains=filter_val)

        return new_queryset

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)

        context['orderby'] = self.request.GET.get('orderby', 'id')

        context['filter'] = self.request.GET.get(
            'filter',None)

        return context



class CartView(LoginRequiredMixin, ListView):
    model = CartItem
    template_name = 'cart.html'
    context_object_name = 'cartitems'

    def get_queryset(self):
        user = self.request.user
        cart = Cart.objects.filter(user=user).filter(active=True).first()

        if cart == None:
            self.cartitems = []
        else:
            self.cartitems = cart.cartitems.all()

        return self.cartitems

    def get_context_data(self, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)

        total = 0

        if len(self.cartitems) == 0:
            context['no_products'] = True

        for ci in self.cartitems:
            total += ci.quantity * ci.product.price

        context['total'] = total

        return context

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('list')

class CreateProductView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'create.html'
    fields = '__all__'
    success_url = reverse_lazy('list')

class DetailProductView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'detail.html'
    context_object_name = 'product'

class UpdateProductView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'update.html'
    context_object_name = 'product'
    fields = '__all__'
    success_url = reverse_lazy('list')

class DeleteProductView(PermissionRequiredMixin, DeleteView):
    permission_required = ['products.delete_product', ]

    model = Product
    template_name = 'delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('list')


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


