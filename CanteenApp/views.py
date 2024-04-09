from django.shortcuts import render, redirect
from .models import FoodItem, Order
from django.contrib import messages
from django.db.models import Sum

def Home(request):
    items = FoodItem.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        FoodItem.objects.create(name=name, price=price)
        messages.success(request, 'Item added successfully')
        return redirect('CanteenApp:homeurl')  
    return render(request, 'home.html', {'items': items})

def update(request, item_id):
    item = FoodItem.objects.get(pk=item_id)
    if request.method =='POST':
        item.name = request.POST['name']
        item.price = request.POST['price']
        item.save()
        messages.success(request, 'Item updated successfully')
        return redirect('CanteenApp:homeurl')
    return render(request, 'update.html', {'item': item})

def delete(request, item_id):
    item = FoodItem.objects.get(pk=item_id)
    item.delete()
    messages.success(request, 'Item deleted successfully')
    return redirect('CanteenApp:homeurl')

def order(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        item_ids = request.POST.getlist('item_id')
        quantities = request.POST.getlist('quantity')

        total_price = 0
        for item_id, quantity in zip(item_ids, quantities):
            item = FoodItem.objects.get(pk=item_id)
            quantity = int(quantity)
            total_price += item.price * quantity
            Order.objects.create(username=username, phone=phone, item=item, quantity=quantity, total_price=item.price * quantity)

        return redirect('CanteenApp:summaryurl')
    else:
        items = FoodItem.objects.all()
        return render(request, 'order.html', {'items': items})

def order_summary(request):
    order = Order.objects.last()
    total_price = order.total_price
    return render(request, 'order_summary.html', {'total_price': total_price})
