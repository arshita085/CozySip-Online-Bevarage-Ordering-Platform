"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name= 'index'),
    path('about', views.about, name= 'about'),
    path('cart', views.cart, name= 'cart'),
    
    path('checkout', views.checkout, name= 'checkout'),
    path('checkoutread', views.checkoutread, name= 'checkoutread'),
    path('contact_us', views.contact_us, name= 'contact_us'),
    path('gallery', views.gallery, name= 'gallery'),
    path('my_account', views.my_account, name= 'my_account'),
    path('shop_detail/<int:id>/', views.shop_detail, name= 'shop_detail'),
    path('add_to_cart/<int:id>', views.add_to_cart, name='add_to_cart'),
    path('cart_remove/<int:id>', views.cart_remove, name='cart_remove'),
    path('increment/<int:id>', views.increment, name='increment'),
    path('decrement/<int:id>', views.decrement, name='decrement'),
    path('shop', views.shop, name= 'shop'),
    path("wishlist/", views.wishlist, name="wishlist"),
    path("add_to_wishlist/<int:id>/", views.add_to_wishlist, name="add_to_wishlist"),
    path("wishlist_remove/<int:id>/", views.wishlist_remove, name="wishlist_remove"),
    path('login', views.login, name= 'login'),
    path('logout', views.logout, name= 'logout'),
    path('forget', views.forget, name= 'forget'),
    path('confirm_password', views.confirm_password, name= 'confirm_password'),
    path('register', views.register, name= 'register'),
    path('search/', views.search, name= 'search'),
    path('apply_coupon', views.apply_coupon, name='apply_coupon'),
    
    path('order', views.order, name= 'order'),
    path('orderread', views.orderread, name= 'orderread'),
    
    
    
]