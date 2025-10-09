from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model





class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    token = serializers.CharField(source='get_token', read_only=True)

    class Meta:
        model = get_user_model ()
        fields = ['id', 'username', 'email', 'password', 'token']

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        token = Token.objects.create(user=user)
        return user

class LoginViewSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)

    def create(self, validated_data):
        user = User.objects.get(username=validated_data['username'])
        token, created = Token.objects.get_or_create(user=user)
        return {'username': user.username, 'token': token.key}

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'token']


