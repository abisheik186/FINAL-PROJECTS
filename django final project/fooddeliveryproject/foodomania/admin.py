from django.contrib import admin
from .models import Customer_d,restaurant_d,del_agent,dishes_d,cart
# Register your models here.
admin.site.register(Customer_d)
admin.site.register(restaurant_d)
admin.site.register(del_agent)
admin.site.register(dishes_d)
admin.site.register(cart)