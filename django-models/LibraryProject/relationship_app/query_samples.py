from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author.
books_by_author = Book.objects.filter(author__name='Author_name')

# List all books in a library.
books_in_library = Library.objects.get(name='Library_name')

# Retrieve the librarian for a library.
librarian_for_library = Librarian.objects.get(library__name='Library_name')
