from django.db.models import Prefetch
from django.shortcuts import render
from category.models import Category, Region
from product.models import Product, ProductImage

def main(request):
    categories = Category.objects.filter(is_main=True)
    products = Product.objects.prefetch_related(
        Prefetch('images', queryset=ProductImage.objects.filter(is_main=True), to_attr='main_images'))
    locations = Region.objects.all()
    ctx = {
        "categories": categories,
        "products": products,
        "locations": locations
    }
    return render(request, 'index.html', ctx)

def about(request):
    ctx = {

    }
    return render(request, 'about.html', ctx)

def services(request):
    ctx = {

    }
    return render(request, 'services.html', ctx)

def contact(request):
    ctx = {

    }
    return render(request, 'contact.html', ctx)