from django.shortcuts import render
from django.contrib.auth.models import login, logout, authenticate
from django.http import HttpResponse
from django.contrib.auth.forms import usercreationform, AuthenticationForm


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

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', {'user': request.user})
    else:
        return render(request, 'login.html', {'error': 'You must be logged in to view this page'})

def ListView(request):
    return HttpResponse("This is the list view")

def DetailView(request, pk):
    return HttpResponse(f"This is the detail view for item {pk}")

def CreateView(request):
    return HttpResponse("This is the create view")

def UpdateView(request, pk):
    return HttpResponse(f"This is the update view for item {pk}")

def DeleteView(request, pk):
    return HttpResponse(f"This is the delete view for item {pk}")

