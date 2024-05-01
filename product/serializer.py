from rest_framework.serializers import ModelSerializer

from product.models import *


class ProductListSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'price']


class ProductDetailSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CreateProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class UpdateProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        write_only_fields = ['stock']
        read_only_fields = ['title', 'category', 'price']


class DeleteProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
