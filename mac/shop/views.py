from django.db import models
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Products, Contact_table, Order_table, complaint_table, Order_update, cancel_table
from math import ceil
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
import json


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # messages.success(request,f"Hey {username}, you have created your account successfully")
            message = f"Hey {username}, you have created your account successfully"
            success = True
            return redirect('/shop/login/', {'success': success, 'messages': message})
    else:
        form = UserRegisterForm()

    return render(request, 'shop/register.html', {'form': form})


def index(request):
    product = Products.objects.all()
    print(product)
    slide_no = len(product)
    print(slide_no)
    total_slides = slide_no // 3 + ceil(slide_no / 3 - (slide_no // 3))
    params = {'products': product, 'slide_len': total_slides,
              'range': range(1, total_slides + 1)}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


@login_required
def profile(request):
    return render(request, 'shop/profile.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('inputName', '')
        phone = request.POST.get('inputPhone', '')
        email = request.POST.get('inputEmail', '')
        text = request.POST.get('inputTextarea', '')
        print(name)
        cont = Contact_table(name=name, phone=phone, email=email, text=text)
        cont.save()
    return render(request, 'shop/contact.html')


def products(request, myid):
    prod = Products.objects.filter(id=myid)
    print(prod[0].prod_name)
    return render(request, 'shop/product.html', {'product': prod[0]})


def complaint(request):
    if request.method == 'POST':
        # orderId = request.POST.get('comOrderid')
        name = request.POST.get('comName', '')
        print(name)
        email = request.POST.get('comEmail', '')
        print(email)
        subj = request.POST.get('comSub', '')
        msg = request.POST.get('comTextarea', '')
        comp = complaint_table(com_name=name, com_email=email, com_sub=subj, com_msg=msg)
        comp.save()
    return render(request, 'shop/complaint.html')


def tracker(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        print('skdjfb', orderId, email)
        order = Order_table.objects.filter(email=email, odrid=orderId)
        print(order)
        if len(order) > 0:
            update = Order_update.objects.filter(orderId=orderId)
            updates = []
            for item in update:
                updates.append({'text': item.update_desc, 'time': item.upd_time})
                response = json.dumps([updates, order[0].order_details, order[0]], default=str)
            print(order[0].order_details)
            return HttpResponse(response)
        else:
            return HttpResponse('{}')
    return render(request, 'shop/tracker.html')


def checkout(request):
    if request.method == 'POST':
        name = request.POST.get('chkname', '')
        order_details = request.POST.get('orderdetails')
        email = request.POST.get('chkemail', '')
        state = request.POST.get('chkState', '')
        addr = request.POST.get('chkaddr1', '') + ' ' + request.POST.get('chkaddr2', '')
        city = request.POST.get('chkcity', '')
        zipcode = request.POST.get('chkzipcode', '')
        ordr = Order_table(name=name, email=email, state=state,
                           addr=addr, city=city, zipcode=zipcode, order_details=order_details)
        ordr.save()
        ordrid = Order_table.objects.filter(name=name)[0].pk
        update = Order_update(orderId=ordrid,
                              update_desc="Order has been placed successfully")
        update.save()
        success = True
        id = ordrid
        return render(request, 'shop/checkout.html', {'success': success, 'id': id})
    return render(request, 'shop/checkout.html')


def cancel(request):
    return render(request, 'shop/cancel.html')


def cancelorder(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        run = True
        fail = False
        if email == '' or orderId == '':
            fail = True
            run = False
        update = Order_update.objects.filter(orderId=orderId)
        cancl = cancel_table(orderid=orderId, email=email, cancel_date=update[0].upd_time)
        cancl.save()
        order = Order_table.objects.filter(email=email, odrid=orderId)
        update.delete()
        order.delete()
        # print('nhh')
        success = False
        id = ''
        if not update.exists() and run:
            success = True
            id = orderId
    return render(request, 'shop/cancel.html', {'success': success, 'id': id, 'fail': fail})


def replace(request):
    return render(request, 'shop/replace.html')


def replaceorder(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        run = True
        fail = False
        if email == '' or orderId == '':
            fail = True
            run = False
        order = Order_table.objects.filter(email=email, odrid=orderId)
        update = Order_update.objects.filter(orderId=orderId)
        print(update)
        update.delete()
        order.delete()
        print('nhh')
        print(update)
        success = False
        id = ''
        if not update.exists() and run:
            success = True
            id = orderId
    return render(request, 'shop/replace.html', {'success': success, 'id': id, 'fail': fail})
