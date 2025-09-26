from django.test import TestCase
from api.models import Author, Book
from rest_framework import status, response.data
from rest_framework.test import APIClient
from django.contrib.auth.models import User

# Create your tests here.
class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username="tester", password="testpass123")

        # Auth client
        self.client = APIClient()
        self.client.login(username="tester", password="testpass123")

        # Create test author and book
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book = Book.objects.create(
            title="Harry Potter",
            author=self.author,
            publication_year=1997
        )

   def test_author_creation(self):
       response = self.client.post("/api/authors/", {"name": "J.K. Rowling"})
       self.assertEqual(response.status_code, status.HTTP_201_CREATED)
       self.assertEqual(Author.objects.count(), 2)

   def test_book_creation(self):
       response = self.client.post("/api/books/", {
           "title": "Harry Potter",
           "author": self.author.id,
           "publication_year": 1997
       })
       self.assertEqual(response.status_code, status.HTTP_201_CREATED)
       self.assertEqual(Book.objects.count(), 2)
