from django.shortcuts import render
from . models import Product, Category
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    response_data = {
        'banner_caption': {
            'slide1': 'Banner 1',
            'slide2': 'Banner 2',
            'slide3': 'Banner 3'
        },
        'products': {
            'new_arrival': Product.objects.filter(delete_status=1).order_by('-id', 'priority')[:4],
            'great_discount': Product.objects.filter(delete_status=1).order_by('-discount_percent', 'priority')[:4],
            'featured_products': Product.objects.filter(delete_status=1).order_by('priority')[:4]
        },
        'categories': Category.objects.all()
    }
    return render(request, 'products/home.html', response_data)

def category_products(request, pk):
    ctg = Category.objects.get(pk=pk)
    pg = int(request.GET.get('pg', 1))
    product_pages = Paginator(ctg.products.order_by("priority"), 20)
    return render(request, 'products/category_products.html', {'products': product_pages.get_page(pg)})

def details(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'products/details.html', {'product':product})