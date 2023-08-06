from django.shortcuts import render
from django.views import View
from .models import MenuItem, Category, OrderModel

class MenuKantin(View):
    def get(self, request, *args, **kwargs):
        #Get item
        kantin_1 = MenuItem.objects.filter(category__name__contains='Kantin 1')
        kantin_2 = MenuItem.objects.filter(category__name__contains='Kantin 2')
        kantin_3 = MenuItem.objects.filter(category__name__contains='Kantin 3')
        kantin_4 = MenuItem.objects.filter(category__name__contains='Kantin 4')
        
        #Pass into context
        context = {
            'kantin_1': kantin_1,
            'kantin_2': kantin_2,
            'kantin_3': kantin_3,
            'kantin_4': kantin_4,
        }
        return render(request, 'MenuKantin.html', context)
    
    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        
        order_items = {
            'items': []
        }
        
        items = request.POST.getlist('items[]')
        
        for item in items:
            menu_item = MenuItem.objects.get(pk=int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'description': menu_item.description,
                'price': menu_item.price
            }
            
            order_items['items'].append(item_data)  # Use 'append' instead of 'appends'
        
        price = 0
        item_ids = []  # Changed from 'item_id' to 'item_ids'
        
        for item in order_items['items']:  # Corrected the dictionary key
            price += item['price']
            item_ids.append(item['id'])  # Corrected the variable name
        
        order = OrderModel.objects.create(
            price=price,
            name=name,
            )
        order.items.add(*item_ids)
        
        context = {
            'items': order_items['items'],
            'price': price
        }
        
        return render(request, 'costumer/order_confirmation.html', context)  # Corrected the template name

    def item_detail(request, item_id):
        menu_item = MenuItem.objects.get(pk=int(item_id))
        context = {
            'id': menu_item.pk,
        }
        return render(request, 'item_detail.html', context)