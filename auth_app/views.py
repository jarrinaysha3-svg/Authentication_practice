from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def register_page(request):
    if request.method=='POST':
        username= request.POST.get('username')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')

        if password==confirm_password:
            User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,

            )
            return redirect('login_page')
        else:
            print('Both password do not match.')

    return render(request, 'register.html')

def login_page(request):
    if request.method=='POST':
            username= request.POST.get('username')
            password=request.POST.get('password')

            user= authenticate(request, username= username, password=password)

            if user:
                 login(request, user)
                 return redirect('dashboard_page')
            else:
                 print('Invalid Credentials.')

    return render(request, 'login.html')

def dashboard_page(request):
     return render(request, 'dashboard.html')

def logout_view(request):
     logout(request)
     return redirect('login_page')


# Create your views here.
