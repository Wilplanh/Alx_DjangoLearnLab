from django.shortcuts import render
from django.contrib.auth.models import AbstractUser
from django.views import View
from django.http import HttpResponse
from rest_framework import generics
from .serializers import RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


# Create your views here.

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

class LoginView(View):
    def get(self, request):
        return HttpResponse("Login Page")

class ProfileView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = profileSerializer
