from django.urls import path
from . import views

# urls for product pages
urlpatterns = [
    path('', views.home, name='home'),
    path('<pk>', views.category_products, name='products_in_category',),
    path('details/<pk>', views.details, name='details')
]