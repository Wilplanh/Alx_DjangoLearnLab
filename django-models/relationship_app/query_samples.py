from relationship_app.models import author, book, library, librarian

# Query all books by a specific author.
books_by_author = book.objects.filter(author__name='John Doe')

# List all books in a library.
books = book.objects.all()

# Retrieve the librarian for a library.
librarian_for_library = librarian.objects.get(library__name='Central Library')
