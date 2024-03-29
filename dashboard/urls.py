from django.urls import path
from . import views

urlpatterns = [
    path('dashb', views.dashboard, name="dashb"),
    #category
    path('dashb/category/create', views.create_category, name='create_category'),
    path('dashb/category/list', views.categorys, name='categorys'),
    path('dashb/category/update/<str:slug>/', views.category_update, name='category_update'),
    path('dashb/category/delete/<str:slug>/', views.category_delete,name='category_delete'),
    #item
    path('dashb/items/create', views.product_create, name='product_create'),
    path('dashb/items/list', views.products, name='products'),
    path('dashb/items/update/<str:slug>/', views.product_update, name='product_update'),
    path('dashb/items/delete/<str:slug>/', views.product_delete,name='product_delete'),
    path('dashb/items/detail/str:slug>/', views.product_detail,name='product_detail'),
    #authentication
    path('auth/register', views.register_user, name='register_user'),
    path('auth/sign-in', views.sign_in, name='sign_in'),
    path('auth/sign-out', views.sign_out, name='sign_out'),
    #enter
    path('enter-list', views.list_enter, name='list_enter'),
    path('enter-create', views.create_enter, name='create_enter'),
    path('enter-update/<str:slug>/', views.update_enter, name='update_enter'),
    path('enter-delete/<str:slug>/', views.delete_enter, name='delete_enter'),
    #kirim
    path('dashb/items/kirim', views.kirim, name='kirim'),
    path('generate-excel/', views.generate_excel, name='generate_excel'),
    path('import-excel/', views.import_excel, name='import_excel'),

]