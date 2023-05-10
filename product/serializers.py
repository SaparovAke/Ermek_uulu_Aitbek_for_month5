from rest_framework import serializers
from product.models import Product, Review, Category

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars'.split()

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'id name'.split()

class ProductSerializer(serializers.ModelSerializer):
    products_reviews = ReviewSerializer(many=True)
    products_category = CategorySerializer(many=True)
    class Meta:
        model = Product
        fields = 'id title description products_category products_reviews price'.split()
