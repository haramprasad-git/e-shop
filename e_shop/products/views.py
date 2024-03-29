from django.shortcuts import render
from . models import Product, Category
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    category = request.GET.get('ctg', default='')
    if category:
        products = Product.objects.filter(category__name=category)
    else:
        products = {
            'new_arrival': Product.objects.filter(special_category=1, delete_status=1).order_by("-priority"),
            'great_discount': Product.objects.filter(special_category=2, delete_status=1).order_by("-priority"),
            'featured_products': Product.objects.filter(special_category=3, delete_status=1).order_by("-priority")
        }
    response_data = {
        'banner_caption': {
            'slide1': 'Banner 1',
            'slide2': 'Banner 2',
            'slide3': 'Banner 3'
        },
        'products': products,
        'categories': Category.objects.all()
    }
    return render(request, 'products/home.html', response_data)

def category_products(request, ctg):
    pg = int(request.GET.get('pg', 1))
    product_pages = Paginator(Product.objects.filter(category__id=ctg).order_by("-priority"), 20)
    return render(request, 'products/category_products.html', {'products': product_pages.get_page(pg)})

def details(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'products/details.html', {'product':product})