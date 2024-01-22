from django.db import models
from django.contrib.auth.models import AbstractUser


class Region(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class User(AbstractUser):
    region = models.ForeignKey('Region', on_delete=models.CASCADE, null=True, blank=True)
    bio = models.CharField(max_length=150, null=True, blank=True)
    avatar = models.ImageField(upload_to='user-avatar/', null=True, blank=True)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Product(models.Model):
    user = models.ForeignKey('User', on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    sub_category = models.ForeignKey('Sub_category', on_delete=models.CASCADE)
    brand = models.ForeignKey('Brand', on_delete=models.PROTECT, null=True, blank=True)
    color = models.ManyToManyField('Color', blank=True)
    photos = models.ManyToManyField('Image')
    quantity = models.IntegerField(default=0)
    features = models.TextField(null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_sale = models.BooleanField(default=False)
    old_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount_percent = models.IntegerField(default=0)
    is_banner = models.BooleanField(default=False)
    is_delivery = models.BooleanField(default=False)
    rating = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    size_category = models.ForeignKey('Size_category', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=55)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Sub_category(models.Model):
    name = models.CharField(max_length=55)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='img_color/')
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    img = models.ImageField(upload_to='product_img/')


class Size_category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Card(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateField(auto_now=True)
    quantity = models.IntegerField(default=0)


class Saved(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    product = models.ManyToManyField('Product')


class Office(models.Model):
    name = models.CharField(max_length=25)
    number = models.IntegerField()
    region = models.ForeignKey('Region', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    card = models.ManyToManyField('Card')
    pass_number = models.CharField(max_length=20)
    is_delivery = models.BooleanField(default=False)
    extra_phone_number = models.CharField(max_length=255, null=True, blank=True)
    payment_type = models.BooleanField(default=False)
    office = models.ForeignKey('Region', on_delete=models.PROTECT)
    lat = models.FloatField()
    lot = models.FloatField()
    created_at = models.DateField(auto_now=True)

