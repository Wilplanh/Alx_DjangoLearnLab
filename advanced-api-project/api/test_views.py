from django.test import TestCase
from api.models import Author, Book

# Create your tests here.
class AuthorAPITestCase(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="J.K. Rowling")

    def test_author_creation(self):
        self.assertEqual(self.author.name, "J.K. Rowling")
        self.assertIsInstance(self.author, Author)

class BookAPITestCase(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book = Book.objects.create(title="Harry Potter and the Philosopher's Stone", author=self.author)

    def test_book_creation(self):
        self.assertEqual(self.book.title, "Harry Potter and the Philosopher's Stone")
        self.assertIsInstance(self.book, Book)