from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author.
books_by_author = Author.objects.get(name=author_name), objects.filter(author=author)

# List all books in a library.
books_in_library = Library.objects.get(name=library_name).books.all()

# Retrieve the librarian for a library.
librarian_for_library = Librarian.objects.get(library__name=library_name)
