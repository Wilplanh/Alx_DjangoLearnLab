from django.urls import path
from .views import BookListAPIView



urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
]