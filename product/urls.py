from django.urls import path

from product.views import *

urlpatterns = [
    path('products/<int:pk>', ProductDetailView.as_view()),
    path('products/', ProductListView.as_view()),
    path('products/create', CreateProduct.as_view()),
    path('products/<int:pk>/update', UpdateProduct.as_view()),
    path('products/<int:pk>/delete', DeleteProduct.as_view()),
    path('categories/', CategoryListView.as_view()),
    path('categories/<int:pk>', CategoryDetailView.as_view())
]