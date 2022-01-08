from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Banner, ProductAttribute, Product, Category,Brand,Color,Size,CartOrder,CartOrderItems,ProductReview,Wishlist


# Register your models here.
admin.site.register(Size)



class BannerAdmin(admin.ModelAdmin):
    list_display=('alt_text','image_tag')
admin.site.register(Banner,BannerAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display=('title','image_tag')
admin.site.register(Category,CategoryAdmin)


class BrandAdmin(admin.ModelAdmin):
    list_display=('title','image_tag')
admin.site.register(Brand,BrandAdmin)

class ColorAdmin(admin.ModelAdmin):
    list_display=('title','color_bg')
admin.site.register(Color,ColorAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','title','brand','size','status','is_featured')
    list_editable =('status','is_featured')
admin.site.register(Product,ProductAdmin)


class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id','image_tag','product','price','color','size')
admin.site.register(ProductAttribute,ProductAttributeAdmin)

# Order
class CartOrderAdmin(admin.ModelAdmin):
	list_editable=('paid_status','order_status')
	list_display=('user','total_amt','paid_status','order_dt','order_status')
admin.site.register(CartOrder,CartOrderAdmin)

class CartOrderItemsAdmin(admin.ModelAdmin):
    list_display = ('order','invoice_no','item','image','qty','price','total')
admin.site.register(CartOrderItems,CartOrderItemsAdmin)

class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('user','product','review_text','review_rating','get_review_rating')
admin.site.register(ProductReview,ProductReviewAdmin)

admin.site.register(Wishlist)


