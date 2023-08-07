from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
import logging
from .models import MenuItem, NamaKantin, OrderModel
from django.http import HttpResponseRedirect

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
    
    def post(self, request, *args, **kwargs):
        
        new_data = request.POST.getlist('items[]')
        request.session['temp_data'] = new_data
        next_url = request.GET.get('next', None)
        if next_url:
            return redirect(next_url)
        else:
            # Redirect to a default page if 'next' is not provided
            return redirect('home')
        
    
    def process_and_store_data(self, request):
        name = request.user.username
        if 'temp_data' in request.session:
            temp_data = request.session['temp_data']
            del request.session['temp_data']
            
            for item in temp_data:
                menu_item = MenuItem.objects.get(pk=int(item))
                item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price
            }
                
            order_items = {
            'items': []
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
                'price': price,
            }

        return render(request,'success_page',context)