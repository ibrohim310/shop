from django.urls import path
from . import views

urlpatterns = [
    path('dashb', views.dashboard, name="dashb"),
    #category
    path('dashb/category/create', views.create_category, name='create_category'),
    path('dashb/category/list', views.categorys, name='categorys'),
    path('dashb/category/update/<int:id>/', views.category_update, name='category_update'),
    path('dashb/category/delete/<int:id>/', views.category_delete,name='category_delete'),
    #item
    path('dashb/items/create', views.create_product, name='create_product'),
    path('dashb/items/list', views.products, name='products'),
    path('dashb/items/update/<int:id>/', views.product_update, name='product_update'),
    path('dashb/items/delete/<int:id>/', views.product_delete,name='product_delete'),
    #authentication
    path('auth/register', views.register_user, name='register_user'),
    path('auth/sign-in', views.sign_in, name='sign_in'),
    path('auth/sign-out', views.sign_out, name='sign_out'),

]