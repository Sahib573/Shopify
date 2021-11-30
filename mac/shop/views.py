from django.db import models
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Products, Contact_table, Order_table, complaint_table, Order_update
from math import ceil
import json


# Create your views here.

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
                response = json.dumps(updates, default=str)
            return HttpResponse(response)
        else:
            return HttpResponse('{}')
    return render(request, 'shop/tracker.html')


def checkout(request):
    if request.method == 'POST':
        name = request.POST.get('chkname', '')
        email = request.POST.get('chkemail', '')
        state = request.POST.get('chkState', '')
        addr = request.POST.get('chkaddr1', '') + ' ' + request.POST.get('chkaddr2', '')
        city = request.POST.get('chkcity', '')
        zipcode = request.POST.get('chkzipcode', '')
        ordr = Order_table(name=name, email=email, state=state,
                           addr=addr, city=city, zipcode=zipcode)
        ordr.save()
        ordrid = Order_table.objects.filter(name=name)[0].pk
        update = Order_update(orderId=ordrid, update_desc="Order has been placed successfully")
        update.save()
        success = True
        id = ordrid
        return render(request, 'shop/checkout.html', {'success': success, 'id': id})
    return render(request, 'shop/checkout.html')
