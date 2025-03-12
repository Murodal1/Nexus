from django.shortcuts import render
from category.models import Category
from product.models import Product, ProductImage

def main(request):
    categories = Category.objects.filter(is_main=True)
    # products = Product.objects.
    ctx = {
        "categories": categories
    }
    return render(request, 'index.html', ctx)