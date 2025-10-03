from django.shortcuts import render
from django.contrib.auth.models import login, logout, authenticate
from django.http import HttpResponse
from django.contrib.auth.forms import usercreationform


# Create your views here.

def home(request):
    return render(request, 'base.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'base.html')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return render(request, 'base.html')

def register(request):
    if request.method == 'POST':
        form = usercreationform(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'login.html', {'success': 'Account created successfully'})
    else:
        form = usercreationform()
    return render(request, 'register.html', {'form': form})


