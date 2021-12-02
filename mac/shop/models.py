from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField


# Create your models here.

class Products(models.Model):
    prod_id = models.AutoField
    prod_name = models.CharField(max_length=20)
    prod_desc = models.CharField(max_length=300)
    category = models.CharField(max_length=50, default="")
    prod_date = models.DateField()
    price = models.IntegerField(default=0)
    prod_img = models.ImageField(upload_to="shop/images", default="")


class Contact_table(models.Model):
    name = models.CharField(max_length=20, default="")
    phone = models.IntegerField()
    email = models.CharField(max_length=30, default="")
    cid = models.AutoField(primary_key=True)
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Order_table(models.Model):
    order_details = models.CharField(max_length=2500, default='')
    odrid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=39)
    email = models.CharField(max_length=30)
    state = models.CharField(max_length=20)
    addr = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=15)


class complaint_table(models.Model):
    com_id = models.ForeignKey(Order_table, on_delete=models.SET_NULL)
    com_name = models.CharField(max_length=20)
    com_email = models.CharField(max_length=30)
    com_sub = models.CharField(max_length=35)
    com_msg = models.CharField(max_length=300)


class Order_update(models.Model):
    orderId = models.IntegerField(default="")
    update_desc = models.CharField(max_length=1000)
    upd_time = models.DateField(auto_now_add=True)
    upd_id = models.AutoField

    def __str__(self):
        return self.update_desc[0:5] + "..."


class cancel_table(models.Model):
    orderid = models.IntegerField()
    cancel_date = models.DateField()
    email = models.CharField(max_length=30)

    def __str__(self):
        return self.orderid


class employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    Designation = models.CharField(max_length=50)
    Adhaar_id = models.IntegerField()
    joining_date = models.DateField()
    address = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    number = models.IntegerField()

    def __str__(self):
        return self.name


# class customer(models.Model):
#     emp_id = models.AutoField(primary_key=True)
#     Adhaar_id = models.IntegerField()
#     joining_date = models.DateField()
#     address = models.CharField(max_length=100)
#     name = models.CharField(max_length=50)
#     number = models.IntegerField()
#
#     def __str__(self):
#         return self.name


class supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    joining_date = models.DateField()
    address = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    number = models.IntegerField()

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='main.jpg', upload_to='profile_imgs')
    address = models.CharField(max_length=100)
    number = models.IntegerField()

    def __str__(self):
        return f"{self.user.username}'s Profile"
