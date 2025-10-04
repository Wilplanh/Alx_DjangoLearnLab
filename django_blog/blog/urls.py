from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('post/<int:pk>/update/', views.post_update, name='post_update'),
    path('post/<int:pk>/comments/new/', views.CommentCreateView, name='add_comment'),
    path('post/comment/<int:pk>/update/', views.CommentUpdateView, name='edit_comment'),
    path('post/comment/<int:pk>/delete/', views.CommentDeleteView, name='delete_comment'),
    path('search/', views.search_posts, name='search_posts'),
    path('tags/<slug:slug>/', PostByTagListView.as_view(), name='posts_by_tag'),
]
