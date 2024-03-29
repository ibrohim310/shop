from . import serializers
from main import models
from rest_framework import authentication
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from . import custom_permissions


#product

@api_view(['GET'])
def list_products(request):
    products = models.Product.objects.all()
    serializer = serializers.ListProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def product_detail(request, slug):
    user = request.user
    product = models.Product.objects.get(slug=slug)
    image = models.ProductImage.objects.filter(product=product)
    serializer = serializers.DetailProductSerializer(product,image)
    return Response(serializer.data)

#category
@api_view(['GET'])
def category_list(request):
    categorys = models.Category.objects.all()
    serializer = serializers.CategorySerializer(categorys, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def category_detail(request, slug):
    products = models.Product.objects.filter(category_slug = slug)
    serializer = serializers.ListProductSerializer(products, many=True)
    return Response(serializer.data)

#wishlist

@api_view(['POST', 'DELETE'])
def create_wishlist(request, pk=None):
    if request.method == 'POST':
        serializer = serializers.WishListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        try:
            wishlist = models.WishList.objects.get(pk=pk)
        except models.WishList.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        wishlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#view
@api_view(['POST'])
def create_product_review(request):
    serializer = serializers.CreateProductReviewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_product_review(request, slug):
    try:
        review = models.ProductReview.objects.get(slug=slug)
    except models.ProductReview.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = serializers.UpdateProductReviewSerializer(review, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#cart

@api_view(['GET'])
def get_inactive_carts(request):
    carts = models.Cart.objects.filter(is_active=False)
    serializer = serializers.CartSerializer(carts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_active_carts(request):
    carts = models.Cart.objects.filter(is_active=True)
    serializer = serializers.CartSerializer(carts, many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_cart(request, slug):
    try:
        cart = models.Cart.objects.get(slug=slug)
    except models.Cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    cart.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def update_cart_status(request, slug):
    try:
        cart = models.Cart.objects.get(slug=slug)
    except models.Cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    cart.is_active = not cart.is_active
    cart.save()
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def cart_detail(request, slug):
    try:
        cart = models.Cart.objects.get(slug=slug)
    except models.Cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = serializers.CartSerializer(cart)
    return Response(serializer.data)

#cart-product
@api_view(['POST'])
def create_cart_product(request):
    serializer = serializers.CartProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_cart_product(request, slug):
    try:
        cart_product = models.CartProduct.objects.get(slug=slug)
    except models.CartProduct.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = serializers.CartProductSerializer(cart_product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_cart_product(request, slug):
    try:
        cart_product = models.CartProduct.objects.get(slug=slug)
    except models.CartProduct.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    cart_product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)




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





@api_view(['GET'])
def log_in(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        token, _ = Token.objects.get_or_create(user=user)
        data = {
            'token':token.key,
            'status':status.HTTP_200_OK
        }
    else:
        data = {'status':status.HTTP_404_NOT_FOUND}
    return Response(data)


@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = User.objects.create_user(username=username, password=password)
    token = Token.objects.create(user=user)
    return Response({'username':username,
                     'token':token.key}
                     )

@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([custom_permissions.IsSupperUser])
def list_users(request):
    return Response({})