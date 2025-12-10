from django.contrib import admin
from .models import*
# Register your models here.
admin.site.register(user)
admin.site.register(Main_category)
admin.site.register(Sub_category)
admin.site.register(Product)
admin.site.register(Add_cart)
admin.site.register(Wishlist)
admin.site.register(User_coupon)
admin.site.register(Coupon)
admin.site.register(Checkout)
admin.site.register(Order)



