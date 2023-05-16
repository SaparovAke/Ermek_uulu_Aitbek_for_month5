from rest_framework import serializers
from product.models import Product, Review, Category
from rest_framework.exceptions import ValidationError


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars'.split()

class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(required=True, min_length=1, max_length=100)
    stars = serializers.IntegerField(min_value=1, max_value=10)
    product_id = serializers.IntegerField(min_value=1)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'name'.split()

class CategoryValidateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, min_length=1, max_length=100)


class ProductSerializer(serializers.ModelSerializer):
    products_reviews = ReviewSerializer(many=True)
    products_category = CategorySerializer()

    class Meta:
        model = Product
        fields = 'id title description price products_category products_reviews'.split()


class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, min_length=1, max_length=100)
    description = serializers.CharField(required=True)
    products_category_id = serializers.IntegerField(min_value=1)
    price = serializers.IntegerField()

    def valdate_category_id(self, products_category_id): #products_category_id -> does is not exist
        try:
            Category.objects.get(id=products_category_id)
        except Category.DoesNotExist:
            raise ValidationError('Category does not exist!')
        return products_category_id
