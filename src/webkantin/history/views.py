from django.shortcuts import render, get_object_or_404
from django.views import View
from makanan.models import MenuItem, OrderModel

class Order(View):
    def post(self, request, *args, **kwargs):
        name = request.user.username
        
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
            
            order_items['items'].append(item_data)
        
        price = 0
        item_ids = []
        
        for item in order_items['items']:
            price += item['price']
            item_ids.append(item['id'])
        
        order = OrderModel.objects.create(
            price=price,
            name=name,
            jumlah=len(item_ids),
            )
        order.items.add(*item_ids)
        
        context = {
            'items': order_items['items'],
            'price': price
        }
        
        return render(request, 'order.html', context)
