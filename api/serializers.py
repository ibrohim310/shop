from rest_framework import serializers
from main import models

class ListProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'
        # fields = ['id', 'name']
        # exclude = ['id',]

class DetailProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    image = serializers.SlugRelatedField(slug_field='image', read_only=True)
    class Meta:
        model = models.Product
        depth = 1
        fields = ['id', 'name', 'description', 
                  'quantity', 'price', 'currency', 
                  'discount_price', 'baner_image', 
                  'category', 'review', 'is_discount', 
                  'is_active' ]


#wishlist
class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WishList
        fields = '__all__'


#view
class CreateProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductReview
        fields = '__all__'


class UpdateProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductReview
        fields = ['field1', 'field2']

#cart

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cart
        fields = '__all__'

#cartproduct
class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CartProduct
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'

class ListProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductImage
        fields = '__all__'


class ListProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductReview
        fields = '__all__'

class ListEnterProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EnterProduct
        fields = '__all__'


class ListCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cart
        fields = '__all__'


class ListCartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CartProduct
        fields = '__all__'


class ListWishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WishList
        fields = '__all__'