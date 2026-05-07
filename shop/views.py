from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Product

def homepage(request):
    products = Product.objects.all()[:3]
    return render(request, 'shop/homepage.html', {'products': products})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

def add_to_cart(request, product_id):
    cart = request.session.get('cart', [])
    cart.append(product_id)
    request.session['cart'] = cart
    return redirect('cart')

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', [])
    if product_id in cart:
        cart.remove(product_id)
    request.session['cart'] = cart
    return redirect('cart')

def cart_view(request):
    cart = request.session.get('cart', [])
    products = Product.objects.filter(id__in=cart)
    total = sum(p.price for p in products)
    return render(request, 'shop/cart.html', {'products': products, 'total': total})

def checkout(request):
    if request.method == "POST":
        name = request.POST.get("name")
        request.session['cart'] = []
        return redirect(reverse('thank_you') + f"?name={name}")
    return render(request, 'shop/checkout.html')

def thank_you(request):
    name = request.GET.get("name", "Customer")
    return render(request, 'shop/thank_you.html', {'name': name})

# Create your views here.
