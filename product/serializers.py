from rest_framework import serializers
from product.models import Product, Review, Category

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = 'id title description price'.split()
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'