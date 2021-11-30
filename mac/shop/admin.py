from django.contrib import admin

# Register your models here.

from .models import Products, Contact_table, Order_table, complaint_table, Order_update

admin.site.register(Products)
admin.site.register(Contact_table)
admin.site.register(Order_table)
admin.site.register(complaint_table)
admin.site.register(Order_update)
