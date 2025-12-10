from django.shortcuts import render,HttpResponse,redirect
from .models import*
from django.contrib import  messages
from django.utils import timezone
# Create your views here.

def about(request):
    if "email" in request.session:
        return render(request,"about.html")
    else:    
        return redirect("login")
     

def cart(request):
    if 'email' in request.session:
        uid=user.objects.get(email=request.session["email"])

        mc=Main_category.objects.all().order_by("-id")
        sid=Sub_category.objects.all().order_by("-id")
        pid=Product.objects.all().order_by("-id")
        cid=Add_cart.objects.filter(user_id=uid).order_by("-id")
        prod = Add_cart.objects.filter(user_id=uid)
        cart_count=Add_cart.objects.filter(user_id=uid).count()
        wishlist_count=Wishlist.objects.filter(user_id=uid).count()
        ucid=User_coupon.objects.filter(user_id=uid,ex=True).order_by("-id").first()
        

        subtotal = sum(item.total_price for item in cid)
        Shipping = 50
        discount = 0
        total = subtotal + Shipping - discount

        print(ucid)
        l1 = []
        sub_total = 0
        charge = 0
        total_price = 0
        discount=0
        for i in prod:
            a = i.quantity * i.price
            l1.append(a)
            sub_total = sum(l1)
            charge = 50
        total_price = sub_total + charge
        if ucid == None:
            discount=0
        else:  
            discount=ucid.coupon_id.discount
            total_price-=ucid.coupon_id.discount
            print(ucid.coupon_id.discount)
        if cid.count() == 0 and ucid != None:
            ucid.ex=False
            discount=0
            total_price=0
            ucid.save()
        
        
            
        # for i in cid:
        #     print("dfsak",i.size_cart)    


        # prod = Add_to_cart.objects.filter(user_id=uid)
        # prod = Add_to_cart.objects.filter(user_id=uid)
        con={"uid":uid,"mc":mc,"sid":sid,"pid":pid,"cid":cid,"subtotal":subtotal,"Shipping":Shipping,"total_price":total_price,"discount":discount,"cart_count":cart_count,"wishlist_count":wishlist_count,"prod":prod,"total":total,"ucid":ucid}
        

        return render(request,"cart.html",con)
    else:
        return render(request,"login.html")




def increment(request,id):
    if 'email' in request.session:

        cid=Add_cart.objects.get(id=id)  
        
        if cid:  
            cid.quantity = cid.quantity +1
            cid.total_price = cid.quantity * cid.price
            cid.save()
        return redirect("cart")

def decrement(request,id):
    if 'email' in request.session:

        cid=Add_cart.objects.get(id=id)  
        
        if cid: 
            cid.quantity = cid.quantity -1
            if cid.quantity <= 0:
                cid.delete()
            else:
                cid.total_price = cid.quantity * cid.price
                cid.save()

        return redirect("cart")
    
def add_to_cart(request,id):
    if "email" in request.session:
        uid=user.objects.get(email=request.session['email']) 
        pid=Product.objects.get(id=id)
        
        cid = Add_cart.objects.filter(user_id=uid, Product_id=pid).first()
        if cid:
        
            cid.quantity += 1
            cid.total_price = cid.price * cid.quantity
            cid.save()
        else:    
            Add_cart.objects.create(user_id=uid,
                Product_id=pid,  
                name=pid.name,
                image=pid.image,
                price=pid.price,
                quantity=1,
                total_price=pid.price,)
        return redirect("cart")
    else:    
        return redirect("login")  
    
def cart_remove(request,id):
    if 'email' in request.session:

        cid=Add_cart.objects.get(id=id)
        cid.delete()
        return redirect("cart")  
    
def apply_coupon(request):
    
    uid=user.objects.get(email=request.session['email'])
    if request.POST:
        coupon_code = request.POST['code']
        
        ccid=Coupon.objects.filter(coupon_code=coupon_code).exists()
        if ccid:
            ccid1=Coupon.objects.get(coupon_code=coupon_code)
            ucid=User_coupon.objects.filter(user_id=uid, coupon_id=ccid1).exists()
            # check expiry
            if ccid1.expiry_time and ccid1.expiry_time < timezone.now():
                messages.error(request, "This coupon has expired.")
                return redirect("cart")
            if ucid:
                messages.info(request, "You have already used this coupon.")
                return redirect("cart")
            else:
                User_coupon.objects.create(user_id=uid, coupon_id=ccid1,ex=True)
                messages.success(request, "Coupon applied successfully!")
                return redirect("cart")
    
        else:
            messages.error(request, "Invalid coupon code .")
            return redirect("cart")

    else:
        return render(request,"cart.html")        
    
def wishlist(request):
    if "email" in request.session:
        uid = user.objects.get(email=request.session['email'])
        wishlist_items = Wishlist.objects.filter(user_id=uid)  
        return render(request, "wishlist.html", {"wishlist_items": wishlist_items})
    else:
        return redirect("login")

def add_to_wishlist(request, id):
    if "email" in request.session:
        uid = user.objects.get(email=request.session['email']) 
        pid = Product.objects.get(id=id)
        
       
        wid = Wishlist.objects.filter(user_id=uid, Product_id=pid).first()
        if wid:
           
            wid.delete()
        else:
            Wishlist.objects.create(
                user_id=uid,
                Product_id=pid,  
                name=pid.name,
                image=pid.image,
                price=pid.price,
            )
        return redirect("shop")   
    else:    
        return redirect("login") 
    
    
def wishlist_remove(request,id):
    if 'email' in request.session:
        wid=Wishlist.objects.get(id=id)
        wid.delete()
        return redirect("wishlist")     
def checkout(request):
    if "email" in request.session:
        uid=user.objects.get(email=request.session["email"])
        mc = Main_category.objects.all().order_by("-id")
        sid = Sub_category.objects.all().order_by("-id")
        pid = Product.objects.all().order_by("-id")
        prod = Add_cart.objects.filter(user_id=uid)
        # cid=Add_cart.objects.filter(user_id=uid).order_by("-id")
        cart_count=prod.count()
        wishlist_count = Wishlist.objects.filter(user_id=uid).count()
        ucid=User_coupon.objects.filter(user_id=uid,ex=True).order_by("-id").first()
        print("checkout item", prod)
 
        subtotal = sum(item.total_price for item in prod)
        Shipping = 50
        discount = 0
        total_price = subtotal + Shipping - discount
        
        # ✅ If cart is empty
        if cart_count == 0:
            if ucid:
                ucid.ex = False  # deactivate coupon
                ucid.save()
            discount = 0
            total_price = 0
            messages.warning(request, "Your cart is empty. Please add items before proceeding to checkout.")
            return redirect("cart")
        
        if ucid:
            discount = ucid.coupon_id.discount
            total_price -= discount
            print("Applied discount:", discount)
        
         # ✅ Razorpay payment creation with exception handling
        try:
            client = razorpay.Client(auth=('rzp_test_uqhoYnBzHjbvGF', 'jEhBs6Qp9hMeGfq5FyU45cVi'))
            response = client.order.create({
                'amount': int(total_price * 100),  # Razorpay expects amount in paise
                'currency': 'INR',
                'payment_capture': 1
            })
            print("Razorpay response:", response)
        except Exception as e:
            print("Razorpay Error:", e)
            messages.error(request, "Error while initiating payment. Please try again later.")
            return redirect("cart")
        
        con={"mc":mc,
            "sid":sid,
            "pid":pid,
            "ucid":ucid,
            "prod":prod,
            "uid":uid,
            "cart_count":cart_count,
            "Shipping":Shipping,
            "subtotal":subtotal,
            "discount":discount,
            "total_price":total_price,
            "wishlist_count":wishlist_count,
            "response":response,
            }
    
        return render(request,"checkout.html",con)
    else:    
        return redirect("login")

def checkoutread(request):
    checkoutdata=Checkout.objects.all().order_by("-id")
    cont={"checkoutdata":checkoutdata}
    return render(request,"checkout.html",cont)

def contact_us(request):
    if "email" in request.session:
        return render(request,"contact_us.html")
    else:    
        return redirect("login")

def gallery(request):
    if "email" in request.session:
        return render(request,"gallery.html")
    else:    
        return redirect("login")

def index(request):
    if "email" in request.session:
        return render(request,"index.html")
    else:    
        return redirect("login")

def my_account(request):
    if "email" in request.session:
        return render(request,"my_account.html")
    else:    
        return redirect("login")

def shop_detail(request, id):
    if "email" in request.session:
        pid=Product.objects.get(id=id)
        context={"pid":pid}
        
        return render(request,"shop_detail.html",context)
    else:
        return redirect("login")

def shop(request):
    if "email" in request.session:
        uid = user.objects.get(email=request.session['email'])
        mc=Main_category.objects.all()
        mc2=request.GET.get("mc2")
        pid=Product.objects.all()
        if mc2:
            pid=Product.objects.filter(Sub_category=mc2)
        else:
            pid=Product.objects.all()
            
            # wishlist_items = Wishlist.objects.filter(user_id=uid)
        wishlist_ids = list(
            Wishlist.objects.filter(user_id=uid).values_list('Product_id', flat=True)
        )
        
        
        cont={"mc":mc, "pid":pid, "wishlist_ids":wishlist_ids}
        return render(request,"shop.html",cont)
    else:    
        return redirect("login")
    
# def apply_coupon(request):
    
#     uid=user.objects.get(email=request.session['email'])
#     if request.POST:
#         coupon_code = request.POST['code']
        
#         ccid=Coupon.objects.filter(coupon_code=coupon_code).exists()
#         if ccid:
#             ccid=Coupon.objects.get(coupon_code=coupon_code)
#             messages.success(request, "Coupon applied successfully!")
                
    
#         else:
            
#             messages.error(request, "Invalid coupon code .")
#             return redirect("cart")

#     else:
#         return render(request,"cart.html")       




def login(request):
    if "email" in request.session:
        uid=user.objects.get(email=request.session['email'])
        return render(request,"index.html")
    else:
        if request.POST:
            email=request.POST['email']
            password=request.POST['password']
            try:
                uid=user.objects.get(email=email)
                if uid.email==email:
                    request.session["email"]=uid.email
                    if uid.password==password:
                        return redirect("index")         
                    else:
                        cont={"msg":"Password is incorrect"}
                        return render(request,"login.html",cont) 
                else:
                    return render(request,"login.html") 
            except user.DoesNotExist:
                cont={"msg":"Email doesn't exists."}
                return render(request,"login.html",cont)
        return render(request,"login.html")

def logout(request):
    # try:
    del request.session['email']
    # except KeyError:
    #     pass
    return render(request, "login.html")    

def register(request):
    if request.POST:
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
      
        try:
            uid=user.objects.get(email=email)
            if uid.email==email:
                cont={"msg":"This email is already registered."}
                return render(request,"register.html",cont) 
            
        except:  
            
            if password==cpassword:
                user.objects.create(name=name,email=email,password=password)
                return redirect("login")
        
            else:
                cont={"msg":"Password do not match"}
                return render(request,"register.html",cont)
    else:
        return render(request,"register.html")
    
    


import random
from django.core.mail import send_mail

def forget(request):
    if request.method == "POST":
        email = request.POST.get('email')
        otp = random.randint(1000, 9999)
        try:
            uid = user.objects.get(email=email)
            uid.otp = otp
            uid.save()
            send_mail(
                "OTP Verification",
                f"Your OTP is: {otp}",
                'arshitabhikadiya08@gmail.com',
                [email], )
            
            return render(request, "confirm_password.html", {"email": email})
        # except Users.DoesNotExist:
           
        #     return render(request, "forget.html")
        except :
            er = {"msg":"Thid Email is not registered"}
            return render(request, "login.html",er)
    return render(request,"forget.html")


# def confirm_password(request):
#     return render(request, "confirm_password.html")

def confirm_password(request):
    if request.method == "POST":
        email = request.POST.get("email")
        otp = request.POST.get("otp")
        newpassword = request.POST.get("newpassword")
        cpassword = request.POST.get("cpassword")

        try:
            uid = user.objects.get(email=email)

            if str(uid.otp) == str(otp):
                if newpassword == cpassword:
                    uid.password = newpassword 
                    uid.save()
                    return redirect("login")
                else:
                    return render(request, "confirm_password.html", {
                        "msg": "Passwords do not match.",
                        "email": email
                    })
            else:
                return render(request, "confirm_password.html", {
                    "msg": "Invalid OTP.",
                    "email": email
                })

        except user.DoesNotExist:
            return redirect("forget")

    return render(request, "confirm_password.html")



def search(request):
    srh=request.GET.get('srh')
    pid=Product.objects.all()
    if srh:
        pid=Product.objects.filter(name__contains=srh)
        con={"pid":pid,"srh":srh}
        return render(request,"shop.html",con)
    else:
        con={"pid":pid,"srh":srh}
        return render(request, "shop.html",con)
    
    
import razorpay 
def order(request):
    if 'email' in request.session:
        uid=user.objects.get(email=request.session["email"])
        mc=Main_category.objects.all().order_by("-id")
        sid=Sub_category.objects.all().order_by("-id")
        pid=Product.objects.all().order_by("-id")
        prod = Add_cart.objects.filter(user_id=uid)   #cart items
        cart_count=prod.count()   #cart items count
        wishlist_count=Wishlist.objects.filter(user_id=uid).count()
        ucid=User_coupon.objects.filter(user_id=uid,ex=True).order_by("-id").first()

        subtotal = 0
        Shipping = 50
        discount = 0
        total_price=0
        response = None  # 🛠️ Ensures Razorpay response exists
        
        if cart_count > 0:
            subtotal = sum(item.total_price for item in prod)
            total_price = subtotal + Shipping
            
            if ucid:
                discount=ucid.coupon_id.discount
                total_price -=discount
            else:
                if ucid:
                    ucid.ex=False
                    ucid.save()
            
        if request.method == 'POST':
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            country = request.POST.get('country')
            state = request.POST.get('state')
            zipcode = request.POST.get('zipcode')

            # Create and save to database
            Checkout.objects.create(
                fname=fname,
                lname=lname,
                email=email,
                phone=phone,
                address=address,
                country=country,
                state=state,
                zipcode=zipcode,
                # user_id=uid
            )
            # Razorpay integration
            client = razorpay.Client(auth=('rzp_test_uqhoYnBzHjbvGF', 'jEhBs6Qp9hMeGfq5FyU45cVi'))
            response = client.order.create({
                'amount': int(total_price * 100),
                'currency': 'INR',
                'payment_capture': 1
            })
            print("Razorpay response:", response)
                
            for item in prod:
                Order.objects.create(
                    user_id=uid,
                    name=item.name,
                    image=item.image,
                    price=item.price,
                    quantity=item.quantity,
                    total_price=item.total_price,
                )
                item.delete()
                
            return redirect("orderread")
         # Render checkout page
        cont={
            "mc":mc,
            "uid":uid,
            "sid":sid,
            "pid":pid,
            "cart_count":cart_count,
            "wishlist_count":wishlist_count,
            "subtotal":subtotal,
            "cid":prod,
            "Shipping":Shipping,
            "discount":discount,
            "total_price":total_price,
            "ucid":ucid,   
            "response":response         
            
        }
        return render(request,"checkout.html",cont)
    else:
        return redirect("login")


def orderread(request):
    if 'email' in request.session:
        oid=Order.objects.all()
        con={"oid":oid}
        return render(request,"order.html",con)
        
    
    