from django.contrib import admin
from .models import Category, Subcategory, Product, Cart, Wishlist, Order, Review, DiscountCode, ProductImage

admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Wishlist)
admin.site.register(Order)
admin.site.register(Review)
admin.site.register(DiscountCode)
admin.site.register(ProductImage)
