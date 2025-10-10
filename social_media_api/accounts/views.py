from django.shortcuts import render
from django.contrib.auth.models import AbstractUser
from django.views import View
from django.http import HttpResponse
from rest_framework import generics, permissions
from .serializers import RegisterSerializer, LoginViewSerializer, ProfileSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from rest_framework.generics import GenericAPIView




# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = RegisterSerializer

class LoginView(View):
    def post(self, request):
        serializer = LoginViewSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response(serializer.errors, status=400)

class ProfileView(generics.RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = ProfileSerializer


class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]


class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

