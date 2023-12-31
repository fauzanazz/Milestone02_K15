from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import View

class Index(View):

    def get(self, request):
        return render(request, 'index.html')
class Profile(View):
    def get(self, request):
        return render(request, 'about.html')
    

def loginpage(request):
    # return HttpResponse("Hello world!")
    if request.method=='POST':
        username = request.POST.get("user")
        password = request.POST.get("pass")

        user = authenticate(request,username= username, password= password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.add_message(request, 30, 'Wrong Password or Username.')

    return render (request,'loginpage.html')

def signuppage(request):
    # return HttpResponse("Hello world!")
    if request.method == 'POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            messages.add_message(request, 30, 'Please enter your password corectly!')
        else:
            all_users = User.objects.values()
            isExists = False
            for i in all_users:
                if uname == i['username']:
                    isExists = True

            if isExists:
                messages.add_message(request,30, 'Username already exists')
            else:
                myuser = User.objects.create_user(uname,email,pass1)
                myuser.save()
                return redirect('login')

    return render (request, template_name='signuppage.html')

@login_required(login_url='login')
def homepage(request):
    # return HttpResponse("Hello world!")
    return render (request,'index.html')
