from . import serializers
from main import models

from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def list_products(request):
    products = models.Product.objects.all()
    serializer = serializers.ListProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def list_enter_products(request):
    enters = models.EnterProduct.objects.all()
    serializer = serializers.ListEnterProductSerializer(enters, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def list_product_images(request):
    images = models.ProductImage.objects.all()
    serializer = serializers.ListProductSerializer(images, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def list_carts(request):
    carts = models.Cart.objects.all()
    serializer = serializers.ListCartSerializer(carts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def list_cart_products(request):
    products = models.CartProduct.objects.all()
    serializer = serializers.ListCartProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def list_wishlist(request):
    wishlists = models.WishList.objects.all()
    serializer = serializers.ListWishListSerializer(wishlists, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def list_categorys(request):
    categorys = models.Category.objects.all()
    serializer = serializers.ListCategorySerializer(categorys, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def list_product_reviews(request):
    reviews = models.ProductReview.objects.all()
    serializer = serializers.ListProductReviewSerializer(reviews, many=True)
    return Response(serializer.data)