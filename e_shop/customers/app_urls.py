from django.urls import path
from . import views
# urls for costomer pages
urlpatterns = [
    path('auth/', views.authentication, name='signup-login'),
    path('auth/logout', views.logout, name='logout'),
    path('add/address/', views.add_address, name='add-address')
]