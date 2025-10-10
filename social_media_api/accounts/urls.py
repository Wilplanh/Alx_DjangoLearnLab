from django.urls import path
from .views import RegisterView, LoginView, ProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name=follow),
]
