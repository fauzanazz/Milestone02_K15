from django.shortcuts import render
from django.views import View

class Index(View):
    def get(self, request):
        return render(request, 'index.html')
    
class About(View):
    def get(self, request):
        return render(request, 'about.html')