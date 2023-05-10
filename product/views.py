from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.serializers import ProductSerializer, ReviewSerializer, CategorySerializer
from product.models import Product, Review, Category
from django.db.models import Avg, Count


@api_view(['GET', 'POST'])
def product_list_api_view(request):
    products = Product.objects.all()

    if request.method == 'GET':
        data_dict = ProductSerializer(products, many=True).data
        return Response(data=data_dict)

    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        products_category_id = request.data.get('products_category_id')
        price = request.data.get('price')
        product = Product.objects.create(title=title, description=description, products_category_id=products_category_id, price=price)
        product.save()

        return Response(data=ProductSerializer(product).data)

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'error': 'Product not found'},
                        status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data_dict = ProductSerializer(product, many=False).data
        return Response(data=data_dict)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        product.title = request.data.get('title')
        product.description = request.data.get('description')
        product.products_category_id = request.data.get('products_category_id')
        product.price = request.data.get('price')
        product.save()
        return Response(data=ProductSerializer(product).data)

@api_view(['GET', 'PUT', 'DELETE'])
def Review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Review not found'},
                        status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data_dict = ReviewSerializer(review, many=False).data
        return Response(data=data_dict)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        review.text = request.data.get('text')
        review.stars = request.data.get('stars')
        review.product_id = request.data.get('product_id')

        review.save()
        return Response(data=ReviewSerializer(review).data)

@api_view(['GET', 'POST'])
def Review_list_api_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        data_dict = ReviewSerializer(reviews, many=True).data

        return Response(data=data_dict)

    elif request.method == 'POST':
        text = request.data.get('text')
        stars = request.data.get('stars')
        product_id = request.data.get('product_id')

        review = Review.objects.create(text=text, stars=stars, product_id=product_id)
        review.save()

        return Response(data=ReviewSerializer(review).data)



@api_view(['GET'])
def rating_review_api_view(request):
    review = Review.objects.all()
    rating = Review.objects.aggregate(avg=Avg('stars'))
    data_dict = ReviewSerializer(review, many=True).data
    return Response(data=[data_dict, rating])


@api_view(['GET', 'POST'])
def Category_list_api_view(request):
    if request.method == 'GET':
        categorys = Category.objects.all()
        kolichestvo = Category.objects.aggregate(count=Count('products_category'))
        data_dict = CategorySerializer(categorys, many=True).data

        return Response(data=[data_dict, kolichestvo])

    elif request.method == 'POST':
        name = request.data.get('name')
        category = Category.objects.create(name=name)
        category.save()

        return Response(data=CategorySerializer(category).data)



@api_view(['GET', 'PUT', 'DELETE'])
def Category_detail_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:

        return Response(data={'error': 'category not found'},
                        status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data_dict = CategorySerializer(category, many=False).data
        return Response(data=data_dict)

    elif request.method == "PUT":
        category.name = request.data.get('name')
        category.save()
        return Response(data=CategorySerializer(category).data)

    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)