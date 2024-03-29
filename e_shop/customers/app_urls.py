from django.urls import path
from . import views
# urls for costomer pages
urlpatterns = [
    path('signup/', views.signup)
]