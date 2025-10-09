from django.shortcuts import render
from django.contrib.auth.models import AbstractUser
from django.views import View
from django.http import HttpResponse
# Create your views here.

class register(View):
    def get(self, request):
        return HttpResponse("Register Page")
