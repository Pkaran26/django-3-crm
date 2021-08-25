from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/', views.product, name='products'),
    path('customer/<int:pk>/', views.customer, name='customer'),
]
