from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Sizes, Categories
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from cart.forms import CartAddProductForm
from cart.cart import Cart


def index(request, slug_category=None):
    category = Categories.objects.all()
    product = Product.objects.all().order_by('-date')
    selected_category = ''

    if slug_category:
        category = Categories.objects.all()
        selected_category = get_object_or_404(Categories, slug_category=slug_category)
        product = Product.objects.filter(category=selected_category).order_by('-id')

    context = {
        'category': category,
        'product': product,
    }
    return render(request, 'main/index.html', context)


def shop(request):
    produ = Product.objects.all()
    product_list = Product.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(product_list, 6)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    context = {
        'produ': produ,
        'products': products,
    }
    return render(request, 'main/shop.html', context)


def product(request, slug_product):
    product = get_object_or_404(Product, slug_product__iexact=slug_product)
    cart_product_form = CartAddProductForm()
    cart = Cart(request)
    context = {                                               
        'product': product,
        'cart_product_form': cart_product_form,
        'cart': cart,
    }
    return render(request, 'main/product-details.html', context)


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    return render(request, 'main/contact.html')


