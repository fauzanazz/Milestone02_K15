from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import MenuItem, NamaKantin, OrderModel

# class MenuKantin(View):
#     # def get(self, request, *args, **kwargs):
#     #     #Get item
#     #     kantin_1 = MenuItem.objects.filter(NamaKantin__name__contains='Kantin 1')
#     #     kantin_2 = MenuItem.objects.filter(NamaKantin__name__contains='Kantin 2')
#     #     kantin_3 = MenuItem.objects.filter(NamaKantin__name__contains='Kantin 3')
#     #     kantin_4 = MenuItem.objects.filter(NamaKantin__name__contains='Kantin 4')
        
#     #     #Pass into context
#     #     context = {
#     #         'kantin_1': kantin_1,
#     #         'kantin_2': kantin_2,
#     #         'kantin_3': kantin_3,
#     #         'kantin_4': kantin_4,
#     #     }
#     #     return render(request, 'MenuKantin.html', context)
    
#     def get(self, request, *args, **kwargs):
#         kantins = MenuItem.objects.all()
        
#         context = {
#             'kantins': kantins,
#         }
#         return render(request, 'kantin.html', context)
    
#     def post(self, request, *args, **kwargs):
#         name = request.POST.get('name')
        
#         order_items = {
#             'items': []
#         }
        
#         items = request.POST.getlist('items[]')
        
#         for item in items:
#             menu_item = MenuItem.objects.get(pk=int(item))
#             item_data = {
#                 'id': menu_item.pk,
#                 'name': menu_item.name,
#                 'description': menu_item.description,
#                 'price': menu_item.price
#             }
            
#             order_items['items'].append(item_data)
        
#         price = 0
#         item_ids = []
        
#         for item in order_items['items']:
#             price += item['price']
#             item_ids.append(item['id'])
        
#         order = OrderModel.objects.create(
#             price=price,
#             name=name,
#             )
#         order.items.add(*item_ids)
        
#         context = {
#             'items': order_items['items'],
#             'price': price
#         }
        
#         return render(request, 'order.html', context)

#     def food_detail(request, item_id):
#         menu_item = MenuItem.objects.get(pk=int(item_id))
#         context = {
#             'id': menu_item.pk,
#         }
#         return render(request, 'item_detail.html', context)
    
# class AllNamaKantin(View):
#     def get(self, request, *args, **kwargs):
#         kantins = NamaKantin.objects.all()
        
#         context = {
#             'kantins': kantins,
#         }
#         return render(request, 'kantin.html', context)
    
#     def kantin_detail(self, request, kantin_name, *args, **kwargs):
#         kantin = get_object_or_404(NamaKantin, name=kantin_name)
#         menu_items = MenuItem.objects.filter(NamaKantin=kantin)
        
#         context = {
#             'kantin': kantin,
#             'menu_items': menu_items,
#         }
#         return render(request, 'MenuKantin.html', context)

class AllNamaKantin(View):
    def get(self, request, *args, **kwargs):
        all_kantins = NamaKantin.objects.all()
        context = {
            'all_kantins': all_kantins,
        }
        return render(request, 'kantin.html', context)

class KantinDetail(View):
    def get(self, request, kantin_name, *args, **kwargs):
        kantin = get_object_or_404(NamaKantin, name=kantin_name)
        menu_items = MenuItem.objects.filter(NamaKantin=kantin)
        context = {
            'kantin': kantin,
            'menu_items': menu_items,
        }
        return render(request, 'MenuKantin.html', context)
    
class FoodDetail(View):
    def get(self, request, item_id, *args, **kwargs):
        menu_item = get_object_or_404(MenuItem, pk=item_id)
        context = {
            'menu_item': menu_item,
        }
        return render(request, 'item_detail.html', context)