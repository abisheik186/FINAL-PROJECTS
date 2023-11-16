# views.py

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from decimal import Decimal
# from django.contrib.auth import login,logout,authenticate
import random
from .models import Customer_d,OTP_d,restaurant_d,del_agent,dishes_d,cart  # Create a model to store OTPs temporarily
def homepage(request):
    restaurants=restaurant_d.objects.all()
    return render(request,'homepage.html',{'restaurants':restaurants})
def home(request):
    restaurants=restaurant_d.objects.all()
    return render(request,'index.html',{'restaurants':restaurants})

def login(request):    
    global customer
    if request.method == 'POST':
            cusemail=request.POST.get('email')
            password=request.POST.get('password')
            customer=Customer_d.objects.get(email=cusemail,password=password)
            if customer:
                messages.success(request,'logged in succesfully')
                return redirect(home)
            else:
                messages.error(request, 'login failed.')
                return redirect(homepage)
    return render(request,'index.html')
def register(request):
    if request.method == 'POST':
        rname=request.POST.get('rname')
        remail=request.POST.get('remail')
        mobile=request.POST.get('mobile')
        rpassword=request.POST.get('rpassword')
        rcpassword=request.POST.get('rcpassword')
        if rpassword == rcpassword:
            data=Customer_d(name=rname, email=remail,phno=mobile, password=rpassword)
            data.save()
            return redirect(home)
        else:
            pwmissmatch='password does not match'
    return render(request,'index.html')
def res_register(request):
    if request.method == 'POST'and request.FILES.get('image'):
        rname=request.POST.get('resrname')
        remail=request.POST.get('resremail')
        rpassword=request.POST.get('resrpassword')
        rcpassword=request.POST.get('resrcpassword')
        uploaded_image = request.FILES['image']

        if rpassword == rcpassword:
            data=restaurant_d(res_name=rname, res_email=remail, res_password=rpassword, image=uploaded_image)
            data.save()
            print('data stored successfully')
            return redirect(home)
        else:
            pwmissmatch='password does not match'
    return render(request,'index.html')

def res_login(request):    
    global reslemail
    if request.method == 'POST':
            reslemail=request.POST.get('email')
            reslpassword=request.POST.get('password')
            if restaurant_d.objects.filter(res_email=reslemail,res_password=reslpassword):
                messages.success(request,'logged in succesfully')
                return redirect(adddish)
            else:
                messages.error(request, 'login failed.')
                return redirect(home)
    return render(request,'index.html')

def dishes(request,id):
    res_dishes=dishes_d.objects.filter(restaurant=id)
    return render(request,'dishes.html',{'res_dishes':res_dishes})

def adddish(request):
    drestaurant=restaurant_d.objects.get(res_email=reslemail)
    if request.method=='POST':
        dname=request.POST.get('dname')
        dprice=request.POST.get('dprice')
        ddescription=request.POST.get('ddescription')
        dimage=request.FILES['dimage']
        dish=dishes_d(name=dname,price=dprice,description=ddescription,image=dimage,restaurant=drestaurant)
        dish.save()
    return render(request,'restaurant.html')

@csrf_exempt
def addtocart(request):
    dish_id=request.POST.get("dish_id")
    quantity=request.POST.get("quantity")
    dish=dishes_d.objects.get(id=dish_id)
    dishprice=dishes_d.objects.get(id=dish_id).price
    total=(float(quantity)*dishprice)
    cartdets=cart(customer_dets=customer,dishes=dish,quantity=quantity,total=total)
    cartdets.save()
    """
    if request.method=='POST':
        id=request.POST.get('pk')
        quantity=request.POST.get('quantity')
        dish_dets=dishes_d.objects.get(id=id)
    return render(request,'dishes.html')"""
    return JsonResponse({"Success":"Added"})

def cartfunc(request):
    cart_items=cart.objects.filter(customer_dets=customer,status='Not Paid')
    total_values=[]
    for i in cart_items:
        total_values.append(i.total)
    total=sum(total_values)
    return render(request,'cart.html',{'cart_items':cart_items,'total': total})

def afterpayment(request):
    if request.method == 'POST':
        cart.objects.filter(customer_dets=customer,status='Not Paid').update(status='Paid')
        return redirect(home)
    return render(request,'paymentpage.html')









def generate_otp():
    return str(random.randint(1000, 9999))

def send_otp(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        otp = generate_otp()
        
        # Save the OTP temporarily (you can use caching or a database)
        OTP_d.objects.create(otpemail=email, otp=otp)

        # Send the OTP via email
        subject = 'Your OTP for Verification'
        message = f'Your OTP is: {otp}'
        from_email = 'your_email@gmail.com'
        recipient_list = [email]

        try:
            send_mail(subject, message, from_email, recipient_list)
            messages.success(request, 'OTP sent successfully!')
            return redirect('verify_otp')  # Redirect to OTP verification page
        except Exception as e:
            messages.error(request, 'Failed to send OTP. Please try again.')
    
    return render(request, 'send_otp.html')

def verify_otp(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        email = request.POST.get('email')

        # Retrieve the stored OTP
        stored_otp = OTP_d.objects.get(otpemail=email).otp

        if entered_otp == stored_otp:
            messages.success(request, 'OTP verified successfully!')
            OTP_d.objects.filter(otpemail=email).delete()
            # Add your logic for further authentication or actions here
        else:
            messages.error(request, 'OTP verification failed. Please try again.')

    return render(request, 'verify_otp.html')

