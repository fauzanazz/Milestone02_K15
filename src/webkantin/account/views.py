from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')


        # Check if user is exist
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Success")
            return redirect('home')
        else:
            messages.error(request, "Username or Password is wrong")
            return redirect('login')
    return render(request, 'LoginPage.html')

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration succes"))
    else:
        form = UserCreationForm()
            
    return render(request, 'Register.html',{
        "form": form,
    })
    
    # if request.method == 'POST':
    #     uname=request.POST.get('username')
    #     email=request.POST.get('email')
    #     pass1=request.POST.get('password1')
    #     pass2=request.POST.get('password2')

    #     if pass1!=pass2:
    #         messages.success(request, ("Password mu tidak sama"))
    #     else:
    #         myuser = User.objects.create_user(uname,email,pass1)
    #         myuser.save()
    #         return redirect('login')

    # return render (request, template_name='signuppage.html')

def logout_user(request):
    logout(request)
    messages.success(request, "Logout Success")
    return redirect('login')