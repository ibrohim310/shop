from . import views
from django.urls import path

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:id>', views.product_detail, name='product_detail'),
    path('carts', views.carts, name='carts'),
    path('cart/<int:id>/', views.cart_detail, name='cart_detail'),
    path('cart/detail/delete/', views.cart_detail_delete, name='cart_detail_delete')
    
]