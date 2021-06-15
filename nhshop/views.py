from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
def store(request):
    total_item = 0
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.order_item_set.all()

    else:
        items = []
    for item in items:
        total_item+= item.quantity
    products = Product.objects.all()
    print(products)
    context = {'products':products,'total_item':total_item}
    return render(request,'nhshop/store.html',context)

def cart(request):
    total_item = 0
    total_price = 0
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.order_item_set.all()
    else:
        items = []
    for item in items:
        total_item+=item.quantity
        total_price+=(item.product.price * item.quantity)
    context = {'items':items,'total_item':total_item,'total_price':total_price}
    return render(request,'nhshop/cart.html',context)

def checkout(request):
    total_item = 0
    total_price = 0
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.order_item_set.all()
        print(items)

    else:
        items = []
    for item in items:
        total_item+=item.quantity
        total_price+=(item.product.price * item.quantity)
    context = {'items':items,'total_item':total_item,'total_price':total_price}
    return render(request,'nhshop/checkout.html',context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action',action)
    print('Product',productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer,complete=False)
    orderItem, created = Order_Item.objects.get_or_create(order=order,product=product)

    if action == "add":
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == "remove":
        orderItem.quantity = (orderItem.quantity - 1)
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse("item was added",safe=False)
