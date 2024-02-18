from django.urls import path
from . import views

urlpatterns = [
    path('product-list/', views.list_products),
    path('product-detail/<int:id>/', views.product_detail),
    path('categorys', views.category_list),
    path('category-detail/<int:id>/', views.category_detail),
    path('cart-product/create/', views.create_cart_product),
    path('cart-product/update/<int:id>/', views.update_cart_product),
    path('cart-product/delete/<int:id>/', views.delete_cart_product),
    path('cart/get-inactive/', views.get_inactive_carts),
    path('cart/get-active/', views.get_active_carts),
    path('cart/delete/<int:id>/', views.delete_cart),
    path('cart/update-status/<int:id>/', views.update_cart_status),
    path('cart/detail/<int:id>/', views.cart_detail),
    path('wishlist/create/', views.create_wishlist),
    
]