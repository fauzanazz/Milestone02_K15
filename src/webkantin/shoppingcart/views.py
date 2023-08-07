from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

class Cart(View):
    def get(self, request, *args, **kwargs):
        item_carts = request.POST.get("items")
        user = item_carts.user
        items = item_carts.name
