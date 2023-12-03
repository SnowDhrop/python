from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.urls import reverse

from store.models import Cart, Order, Product

def index (request):
    products = Product.objects.all()
    return render(request, 'store/index.html', {"products": products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/detail.html', context={"product": product})

def add_to_cart(request, slug):
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    cart, _ = Cart.objects.get_or_create(user=user)
    order, created = Order.objects.get_or_create(user=user, product=product)

    if created:
        cart.orders.add(order)
        cart.save()
    else:
        order.qty += 1
        order.save()

    return redirect(reverse("product", kwargs={"slug": slug}))