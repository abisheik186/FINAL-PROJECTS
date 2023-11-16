from django.db import models

class Customer_d(models.Model):
    name=models.CharField(max_length=50)
    phno=models.CharField(max_length=20)
    email=models.EmailField(unique=True)
    password = models.CharField(max_length=32)

class restaurant_d(models.Model):
    res_name=models.CharField(max_length=100)
    res_email=models.EmailField(unique=True)
    res_password=models.CharField(max_length=32)
    image=models.ImageField(upload_to='restaurantsimages/',blank=True,null=True)

class del_agent(models.Model):
    del_name=models.CharField(max_length=100)
    del_email=models.EmailField(unique=True)
    del_password=models.CharField(max_length=32)

class OTP_d(models.Model):
    otpemail=models.EmailField(unique=True)
    otp=models.CharField(max_length=6)

class dishes_d(models.Model):
    name=models.CharField(max_length=200)
    price=models.FloatField()
    description=models.TextField()
    image=models.ImageField(upload_to='dish_uploads/',blank=True,null=True)
    restaurant=models.ForeignKey(restaurant_d,on_delete=models.CASCADE,default=None)

class cart(models.Model):
    customer_dets=models.ForeignKey(Customer_d,on_delete=models.CASCADE,default=None)
    dishes=models.ForeignKey(dishes_d,on_delete=models.CASCADE,default=None)
    quantity=models.IntegerField()
    total=models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    status=models.CharField(max_length=20, default='Not Paid')