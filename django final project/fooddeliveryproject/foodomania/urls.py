"""
URL configuration for fooddeliveryproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from foodomania import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('cus_homepage',views.home,name='home'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('restaurantlogin',views.res_login,name='restaurantlogin'),
    path('restaurantregister',views.res_register,name='restaurantregister'),
    path('adddish',views.adddish,name='adddish'),
    path('restaurant/dishes/<int:id>',views.dishes,name='dishes'),
    path('restaurant/dishes/cart',views.cartfunc,name='cart'),
    path('restaurant/dishes/cart/addtocart',views.addtocart,name='addtocart'),
    path('restaurant/dishes/cart/afterpayment',views.afterpayment,name='paymentdone'),
    path('email',views.send_otp,name='send_otp'),
    path('otp',views.verify_otp,name='verify_otp'),
]
