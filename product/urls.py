from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.products_view, name='products'),
    path('create-product/', views.create_product_view, name='create-product'),

    ]