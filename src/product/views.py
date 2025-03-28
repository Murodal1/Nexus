from django.shortcuts import render
from .models import Product, Category, Region, ProductImage, ProductView, Profile
from django.db.models import Prefetch, Count, Sum
from django.core.paginator import Paginator

def product_list(request):
    page = request.GET.get('page', 1)
    categories = Category.objects.filter(is_main=True)
    locations = Region.objects.all()
    products = Product.objects.prefetch_related(
        Prefetch('images', queryset=ProductImage.objects.filter(is_main=True), to_attr='main_images'))
    paginator = Paginator(products, 2)
    page_obj = paginator.get_page(page)
    prd_count = Category.objects.annotate(prd_c=Count("product__id"))
    ctx = {
        "categories": categories,
        "locations": locations,
        "products": products,
        "prd_count": prd_count,
        "page_obj": page_obj,
        'count': paginator.count
    }
    return render(request, 'products.html', ctx)


def product_detail(request, pk):
    products = Product.objects.prefetch_related(
        Prefetch('images', queryset=ProductImage.objects.filter(pk=pk), to_attr='main_images'))
    product = Product.objects.get(pk=pk)
    prd_view = ProductView.objects.all()
    profile = Profile.objects.all()
    ctx = {
        "product": product,
        "products": products,
        "prd_view": prd_view,
        "profiles": profile
    }
    return render(request, 'detail.html', ctx)

def product_add(request):
    ctx = {

    }
    return render(request, 'product_add.html', ctx)