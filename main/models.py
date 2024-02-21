from django.db import models
from django.contrib.auth.models import User
from functools import reduce
from datetime import datetime
import slug
from unidecode import unidecode
from .funcs import code_generator

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(blank=True)
    code_generation = models.CharField(max_length=255, unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug=slug.slug(unidecode(self.name, 'UTF-8'))
        self.code_generation = code_generator()
        super(Category, self).save(*args, **kwargs)

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    currency = models.SmallIntegerField(
        choices=(
            (1,'Dollar'), 
            (2, 'So`m')
            )
    )
    discount_price = models.DecimalField(
        decimal_places=2, 
        max_digits=10, 
        blank=True, 
        null=True
        )
    baner_image = models.ImageField(upload_to='baner/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(blank = True)


    @property
    def review(self):
        reviews = ProductReview.objects.filter(product_id=self.id)
        result = reduce(lambda result, x: result + x.mark, reviews, 0)
        try:
            result = round(result / reviews.count())
        except ZeroDivisionError:
            result = 0
        return result

    @property 
    def is_discount(self):
        if self.discount_price is None:
            return 0
        return self.discount_price > 0
    
    @property 
    def is_active(self):
        return self.quantity > 0
    

    def save(self, *args, **kwargs):
        self.slug=slug.slug(unidecode(self.name, 'UTF-8'))
        super(Product, self).save(*args, **kwargs)


class ProductImage(models.Model):
    image = models.ImageField(upload_to='products/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    slug = models.SlugField(blank = True)


    def save(self, *args, **kwargs):
        self.slug=slug.slug(unidecode(self.name, 'UTF-8'))
        super(ProductImage, self).save(*args, **kwargs)


class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    slug = models.SlugField(blank = True)

    def save(self, *args, **kwargs):
        self.slug=slug.slug(unidecode(self.name, 'UTF-8'))
        super(WishList, self).save(*args, **kwargs)


class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    mark = models.SmallIntegerField()
    slug = models.SlugField(blank = True)

    def save(self, *args, **kwargs):
        self.slug=slug.slug(unidecode(self.name, 'UTF-8'))
        super(ProductReview, self).save(*args, **kwargs)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(blank = True)

    @property
    def quantity(self):
        quantity = 0
        products = CartProduct.objects.filter(product_id = self.id)
        for i in products:
            quantity +=i.quantity
        return quantity

    @property
    def total_price(self):
        result = 0
        for i in CartProduct.objects.filter(card_id=self.id):
            result +=(i.product.price)*i.quantity
        return result
    
    def save(self, *args, **kwargs):
        if not self.is_active and not self.date:
            self.date = datetime.now()
        super(Cart, self).save(*args, **kwargs)


    def save(self, *args, **kwargs):
        self.slug=slug.slug(unidecode(self.name, 'UTF-8'))
        super(Cart, self).save(*args, **kwargs)


class CartProduct(models.Model):
    card = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    slug = models.SlugField(blank = True)
    
    @property
    def total_price(self):
        if self.product.is_discount:
            result = self.product.discount_price * self.quantity
        else:
            result = self.product.price * self.quantity
        return result
    

    def save(self, *args, **kwargs):
        self.slug=slug.slug(unidecode(self.name, 'UTF-8'))
        super(CartProduct, self).save(*args, **kwargs)


class EnterProduct(models.Model):
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    product_name = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank = True)

    def __str__(self):
        return f"{self.quantity}"
    
    def save(self, *args, **kwargs):
        self.product_name = self.product.name
        if self.pk:
            enter = EnterProduct.objects.get(pk=self.pk)
            product = enter.product # None/Product
            product.quantity -= enter.quantity
            product.quantity += self.quantity
            product.save()
        else:
            self.product.quantity += self.quantity
            self.product.save()
        super(EnterProduct, self).save(*args, **kwargs)
    
    def save(self, *args, **kwargs):
        if not self.product:
            self.product = Product.objects.create(name=self.product_name)
        super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.slug=slug.slug(unidecode(self.name, 'UTF-8'))
        super(EnterProduct, self).save(*args, **kwargs)


# models.py

