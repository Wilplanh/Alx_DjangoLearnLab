# Django Admin Integration for Book Model

## Steps Performed
1. Registered the `Book` model in `bookshelf/admin.py`.
2. Customized the list display, filters, and search fields.

## Admin Code
```python
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('publication_year',)
    search_fields = ('title', 'author')