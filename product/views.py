from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from product.models import Category
from product.serializer import *


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class CreateProduct(CreateAPIView):
    product = Product.objects.all()
    serializer_class = CreateProductSerializer


class UpdateProduct(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = UpdateProductSerializer


class DeleteProduct(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = DeleteProductSerializer


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
