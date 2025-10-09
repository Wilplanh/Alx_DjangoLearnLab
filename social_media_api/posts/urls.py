from django.urls import path
from .views import PostListCreateView, PostDetailView, CommentListCreateView, CommentDetailView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]