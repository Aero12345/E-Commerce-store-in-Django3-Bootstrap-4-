from typing import Sized
from django.db import models
from django.db.models.fields import PositiveIntegerField
from django.db.models.fields.files import ImageField
from django.utils.html import mark_safe
from PIL import Image
from django.contrib.auth.models import User

# Create your models here.

#Banner

class Banner(models.Model):
    image =models.ImageField(upload_to='banner_images/')

    alt_text =models.CharField(max_length=300)
    class Meta:
        verbose_name_plural='1.Banners'
    
    def image_tag(self):
        return mark_safe('<image src="%s" width="100px" />' % (self.image.url))

    def __dir__(self):
        return self.alt_text

class Category(models.Model):
    title =models.CharField(max_length=100)
    image =models.ImageField(upload_to="cat_images/")

    class Meta:
        verbose_name_plural='2.Categories'

    def image_tag(self):
        return mark_safe('<image src="%s" width="50px" height="50px" />' % (self.image.url))

    def __dir__(self):
        return self.title


class Brand(models.Model):
    title =models.CharField(max_length=100) 
    image =models.ImageField(upload_to="brand_images/")
    class Meta:
        verbose_name_plural='3.Brands'

    def image_tag(self):
        return mark_safe('<image src="%s" width="50" height="15" />' % (self.image.url))

    def __dir__(self):
        return self.title


class Color(models.Model):
    title =models.CharField(max_length=100)
    color_code =models.CharField(max_length=100)
    class Meta:
        verbose_name_plural='4.Colors'
    
    def color_bg(self):
        return mark_safe('<div style="width:50px; height:50px; background-color:%s"></div>' % (self.color_code))

    def __dir__(self):
        return self.title

class Size(models.Model):
    title =models.CharField(max_length=100)
    class Meta:
        verbose_name_plural='5.Sizes'
     
    def __dir__(self):
        return self.title

class Product(models.Model):
    title =models.CharField(max_length=200)
    slug =models.CharField(max_length=400)
    detail =models.TextField()
    specification =models.TextField()
    brand =models.ForeignKey(Brand,on_delete=models.CASCADE)
    category =models.ForeignKey(Category,on_delete=models.CASCADE)
    color =models.ForeignKey(Color,on_delete=models.CASCADE)
    size =models.ForeignKey(Size,on_delete=models.CASCADE)
    status =models.BooleanField(default=True)
    is_featured =models.BooleanField(default=False)
    class Meta:
        verbose_name_plural='6.Products'

    def __dir__(self):
        return self.title


    
#Product Attribute

class ProductAttribute(models.Model):
    product =models.ForeignKey(Product,on_delete=models.CASCADE)
    image =models.ImageField(upload_to='product_images/', null=True)
    color =models.ForeignKey(Color,on_delete=models.CASCADE)
    size =models.ForeignKey(Size,on_delete=models.CASCADE)
    price =models.PositiveIntegerField()
    class Meta:
        verbose_name_plural='7.ProductAttributs'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img=Image.open(self.image.path)

        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)



    def image_tag(self):
        return mark_safe('<image src="%s" width="50" height="15" />' % (self.image.url))


    def __str__(self):
        return self.product.title

# Order
status_choice=(
        ('process','In Process'),
        ('shipped','Shipped'),
        ('delivered','Delivered'),
    )
class CartOrder(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    total_amt=models.FloatField()
    paid_status=models.BooleanField(default=False)
    order_dt=models.DateTimeField(auto_now_add=True)
    order_status=models.CharField(choices=status_choice,default='process',max_length=150)

    class Meta:
        verbose_name_plural='8. Orders'


#order Items
class CartOrderItems(models.Model):
    order=models.ForeignKey(CartOrder,on_delete=models.CASCADE)
    invoice_no=models.CharField(max_length=150)
    item=models.CharField(max_length=150)
    image=models.CharField(max_length=200)
    qty=models.IntegerField()
    price=models.FloatField()
    total=models.FloatField()

    class Meta:
        verbose_name_plural='9.Cart Items'

    def image_tag(self):
        return mark_safe('<image src="/media/%s" width="50" height="15" />' % (self.image))


# Product Review
RATING=(
    (1,'1'),
    (2,'2'),
    (3,'3'),
    (4,'4'),
    (5,'5'),

)
class ProductReview(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    review_text=models.TextField()
    review_rating=models.CharField(choices=RATING,max_length=150)

    def get_review_rating(self):
        return self.review_rating


# WishList
class Wishlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural='Wishlist'

# AddressBook
class UserAddressBook(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    mobile=models.CharField(max_length=50,null=True)
    address=models.TextField()
    status=models.BooleanField(default=False)

    class Meta:
        verbose_name_plural='AddressBook'




