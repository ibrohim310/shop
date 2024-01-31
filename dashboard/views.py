from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from main import models
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


def dashboard(request):
    categorys = models.Category.objects.all()
    products = models.Product.objects.filter(is_active=True)
    users = User.objects.filter(is_satff=False)
    context = {
        'categorys':categorys,
        'products':products,
        'users':users,
    }
    return render(request, 'index.html', context)


def category_list(request):
    categorys = models.Category.objects.all()
    return render(request, 'category/list.html', {'categorys':categorys})


def category_detail(request, id):
    category = models.Category.objects.get(id=id)
    products = models.Product.objects.filter(category=category, is_active=True)
    context = {
        'category':category,
        'products':products
    }
    return render(request, 'category/list.html', context)


def category_update(request, id):
    category = models.Category.objects.get(id=id)
    category.name = request.POST['name']
    category.save()
    return redirect('category_detail', category.id)


def category_delete(request, id):
    category = models.Category.objects.get(id=id)
    category.delete()
    return redirect('category_list')



# CRUD


# dashboard
@login_required(login_url='sign_in')
def dashboard(request):
    
    users = User.objects.all().count()
    products = models.Product.objects.filter().count()
    category = models.Category.objects.all().count()

    context = {
        'users':users,
        'products':products,
        'category':category
    }

    return render(request, 'dashb/index.html', context)


#                                                       category CRUD
def create_category(request):
    if request.method == 'POST':
        models.Category.objects.create(
            name=request.POST['name']
        )
        return redirect('categorys')
    return render(request, 'dashb/category/create.html')


def categorys(request):
    categorys = models.Category.objects.all()
    return render(request, 'dashb/category/list.html', {'categorys':categorys})


def category_update(request, id):
    category = models.Category.objects.get(id=id)
    if request.method == 'POST':
        category.name = request.POST['name']
        category.save()

    return render(request, 'dashb/category/update.html', {'category':category})


def category_delete(request, id):
    models.Category.objects.get(id=id).delete()
    return redirect('category')


#product

def create_product(request):
    if request.method == 'POST':
        name=request.POST['name']
        description=request.POST['description']
        quantity = request.FILES['quantity']
        price = request.FILES['price']
        currency = request.FILES['currency']
        discount_price = request.FILES['discount_price']
        category = models.Category.objects.get(id=request.POST['category_id'])
        baner_image = request.FILES['baner_image']

        models.Product.objects.create(
            name=name,
            quantity=quantity,
            price=price,
            currency=currency,
            discount_price=discount_price,
            description=description,
            category=category,
            baner_image=baner_image
    )
        return redirect('items')
    context = {
        'categorys':models.Category.objects.all(),
    }
    return render(request, 'dashb/items/create.html',context)


def products(request):
    products = models.Product.objects.all()
    context  = {
        'products':products,

    }
    return render(request, 'dashb/items/list.html', context)



def product_update(request, id):
    product = models.Product.objects.get(id=id)
    if request.method == 'POST':
        category = models.Category.objects.get(id=request.POST['category_id'])
        product.name = request.POST['name']
        product.quantity = request.POST['quantity']
        product.price = request.POST['price']
        product.currency = request.POST['currency']
        product.discount_price = request.POST['discount_price']
        product.description = request.POST['description']
        product.category=category
        baner_image = request.FILES.get('baner_image')
        if baner_image:
            product.baner_image=baner_image
        product.save()

    context  = {
        'product':product,
        'categorys':models.Category.objects.all(),
    }

    return render(request, 'dashb/items/update.html', context)


def product_delete(request, id):
    models.Product.objects.get(id=id).delete()
    return redirect('items')


#auth

def register_user(request):
    if request.method == 'POST':
        User.objects.create_user(
            username = request.POST['username'],
            password = request.POST['password']
        )

    return render(request, 'dashb/auth/register.html')


def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashb')
    return render(request, 'dashb/auth/login.html')


def sign_out(request):
    logout(request)
    return redirect('index')




