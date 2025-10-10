from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework,pigmentation import PageNumberPagination

# Create your views here.

# Pagination class
class PostPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = ['title', 'content']


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = PostPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]