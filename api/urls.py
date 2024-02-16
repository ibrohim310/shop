from django.urls import path
from . import views

urlpatterns = [
    path('product-list/', views.list_products),
    path('enter-list/', views.list_enter_products),
    path('image-list/', views.list_product_images),
    path('cartproduct-list/', views.list_cart_products),
    path('cart-list/', views.list_carts),
    path('category-list/', views.list_categorys),
    path('wishlist-list/', views.list_wishlist),
    path('review-list/', views.list_product_reviews)
]