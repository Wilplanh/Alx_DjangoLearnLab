from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.pagination import PageNumberPagination

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


# generates a feed based on the posts from users that the current user follows
class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Get the current user
        user = self.request.user

        # Get all users the current user follows
        following_users = user.following.all()

        # Return posts by followed users, ordered by newest first
        return Post.objects.filter(author__in=following_users).order_by('-created_at')


class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        user = request.user

        # Check if already liked
        if Like.objects.filter(user=user, post=post).exists():
            return Response({"detail": "You already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        # Create Like
        Like.objects.create(user=user, post=post)

        # Create Notification (only if the liker is not the post author)
        if user != post.author:
            Notification.objects.create(
                recipient=post.author,
                actor=user,
                verb="liked your post",
                target=post
            )

        return Response({"detail": "Post liked successfully."}, status=status.HTTP_201_CREATED)


class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        user = request.user

        like = Like.objects.filter(user=user, post=post).first()
        if not like:
            return Response({"detail": "You haven’t liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        like.delete()

        # (Optional) Delete related notification
        Notification.objects.filter(
            recipient=post.author,
            actor=user,
            verb="liked your post",
            target_object_id=post.id
        ).delete()

        return Response({"detail": "Post unliked successfully."}, status=status.HTTP_200_OK) 

class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        # ✅ Use generics.get_object_or_404
        post = generics.get_object_or_404(Post, pk=pk)

        # ✅ Use get_or_create to prevent duplicates
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if not created:
            return Response({"detail": "You already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        # Create notification if liker isn’t the author
        if request.user != post.author:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                target=post
            )

        return Response({"detail": "Post liked successfully."}, status=status.HTTP_201_CREATED)


class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        # ✅ Also use generics.get_object_or_404
        post = generics.get_object_or_404(Post, pk=pk)

        like = Like.objects.filter(user=request.user, post=post).first()
        if not like:
            return Response({"detail": "You haven’t liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        like.delete()

        # Optionally delete the corresponding notification
        Notification.objects.filter(
            recipient=post.author,
            actor=request.user,
            verb="liked your post",
            target_object_id=post.id
        ).delete()

        return Response({"detail": "Post unliked successfully."}, status=status.HTTP_200_OK)