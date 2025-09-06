from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author.
books_by_author = Book.objects.filter(author__name='John Doe')

# List all books in a library.
books = Book.objects.all()

# Retrieve the librarian for a library.
librarian_for_library = Librarian.objects.get(library__name='Central Library')
