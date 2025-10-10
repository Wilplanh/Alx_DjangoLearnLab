from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework import permissions, serializers, generics
from 

# Create your models here.

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)
    

    # Fix the group and permission fields
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )  
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
    

    def __str__(self):
        return self.username


class follow_user(models.Model):
    permissions = [permissions.IsAuthenticated]
    user = models.ForeignKey(CustomUser, related_name='follower', on_delete=models.CASCADE


class unfollow_user(models.Model):
    permissions = [permissions.IsAuthenticated]
    user = models.ForeignKey(CustomUser, related_name='unfollower', on_delete=models.CASCADE)
    unfollowed_user = models.ForeignKey(CustomUser, related_name='unfollowed', on_delete=models.CASCADE)
