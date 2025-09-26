# Book API Endpoints

## Views
- **ListView (GET /books/)** → Retrieve all books (public).
- **DetailView (GET /books/<id>/)** → Retrieve a single book by ID (public).
- **CreateView (POST /books/create/)** → Add a new book (authenticated users).
- **UpdateView (PUT/PATCH /books/<id>/update/)** → Modify an existing book (authenticated users).
- **DeleteView (DELETE /books/<id>/delete/)** → Remove a book (authenticated users).

## Permissions
- Unauthenticated users → read-only access (list, detail).
- Authenticated users → can create, update, and delete.
- Optional: Use `IsAdminOrReadOnly` for stricter control.

## Customizations
- `perform_create`: attaches logged-in user to book.
- `perform_update`: records updater.
- `get_queryset`: allows filtering books by author using query params.

## Testing
Use Postman, curl, or DRF’s browsable API to test all endpoints.


# Book API Advanced Query Features

## Filtering
- Filter books by title, author, or publication_year:
  - `/books/?title=The Hobbit`
  - `/books/?author=1`
  - `/books/?publication_year=2020`

## Searching
- Search by keywords in title or author name:
  - `/books/?search=tolkien`
  - `/books/?search=harry`

## Ordering
- Order by title or publication year:
  - `/books/?ordering=title`
  - `/books/?ordering=-publication_year`



  # API Testing Strategy

## What We Test
- CRUD endpoints for Book model.
- Filtering, searching, ordering.
- Permissions for authenticated vs unauthenticated users.

## Running Tests
Run all tests:
python manage.py test api




The test suite uses Django’s built-in test runner with DRF’s APIClient.  
A separate test database is created automatically and destroyed after tests.  

## Example Cases
- ✅ Create book (authenticated → 201, unauthenticated → 403)
- ✅ Retrieve book by ID (200, correct title returned)
- ✅ Update book (200, title updated in DB)
- ✅ Delete book (204, object removed)
- ✅ Filter/search/order (200, correct query results)