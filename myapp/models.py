from django.db import models

# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=50, blank=True, null=True)
    email=models.EmailField(unique=True, null=True)
    password=models.TextField(max_length=50)
    otp=models.IntegerField(default=0)
    
    
    
    def __str__(self):
        return self.name
    
class Main_category(models.Model):
    name=models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class Sub_category(models.Model): 
    Main_category=models.ForeignKey(Main_category,on_delete=models.CASCADE, blank=True, null=True)
    name=models.CharField(max_length=100, blank=True, null=True)
   
    def __str__(self):
        return self.name   
    
class Product(models.Model):
    Main_category=models.ForeignKey(Main_category,on_delete=models.CASCADE, blank=True, null=True)
    Sub_category=models.ForeignKey(Sub_category,on_delete=models.CASCADE, blank=True, null=True)
    name=models.CharField(max_length=90,blank=True,null=True)
    image=models.ImageField(upload_to="media",blank=True,null=True)
    price=models.IntegerField()
    delete_price=models.IntegerField()
    description=models.TextField()
    
    def __str__(self):
        return self.name 
    
    
class Add_cart(models.Model):
    user_id=models.ForeignKey(user,on_delete=models.CASCADE,blank=True,null=True)
    Product_id=models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True)
    name=models.CharField(max_length=90,blank=True,null=True)
    image=models.ImageField(upload_to="media",blank=True,null=True)
    price=models.IntegerField()
    quantity=models.IntegerField(blank=True,null=True)
    total_price=models.IntegerField()
    
    def __str__(self):
        return self.name
    

class Wishlist(models.Model):
    user_id=models.ForeignKey(user,on_delete=models.CASCADE,blank=True,null=True)
    Product_id=models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True)
    name=models.CharField(max_length=90,blank=True,null=True)
    image=models.ImageField(upload_to="media",blank=True,null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name


class Coupon(models.Model):
    coupon_code=models.CharField(max_length=50,blank=True,null=True)
    discount=models.IntegerField()
    expiry_time = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.coupon_code

class User_coupon(models.Model):
    user_id=models.ForeignKey(user,max_length=60,on_delete=models.CASCADE,blank=True,null=True)
    coupon_id=models.ForeignKey(Coupon,max_length=60,on_delete=models.CASCADE,blank=True,null=True)
    ex=models.BooleanField(blank=True,null=True)  # coupon expire one time use
    expiry_time = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.coupon_id.coupon_code
    
    
class Checkout(models.Model):
    user_id=models.ForeignKey(user,on_delete=models.CASCADE,blank=True,null=True)
    fname=models.CharField(max_length=30,blank=True,null=True)
    lname=models.CharField(max_length=30,blank=True,null=True)
    email=models.EmailField(max_length=30,blank=True,null=True)
    phone=models.IntegerField(blank=True,null=True)
    address=models.TextField(max_length=300,blank=True,null=True)
    country=models.CharField(max_length=30,blank=True,null=True)
    state=models.CharField(max_length=30,blank=True,null=True)
    zipcode=models.IntegerField(blank=True,null=True)
    
    def __str__(self):
        return self.fname
    
class Order(models.Model):
    user_id=models.ForeignKey(user,max_length=60,on_delete=models.CASCADE,blank=True,null=True)
    name=models.CharField(max_length=60,blank=True,null=True)
    order_id=models.CharField(max_length=60,blank=True,null=True)
    image=models.ImageField(blank=True,null=True)
    description=models.CharField(max_length=100,blank=True,null=True)
    size_order=models.CharField(max_length=60,blank=True,null=True)
    quantity=models.CharField(max_length=60,blank=True,null=True)
    price=models.IntegerField()
    total_price=models.IntegerField(default=1,blank=True,null=True)
    time=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    add_date=models.DateTimeField(blank=True,null=True)
    payment_method = models.CharField(max_length=20, default="Online")   # Online / COD
    payment_status = models.CharField(max_length=20, default="Pending")  # Pending / Paid

    
    def __str__(self):
        return self.name
    
    
    
        



    
    
    
    
    
    
    
    
    