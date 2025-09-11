from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .forms import ExampleForm

# Create your views here.

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    # Logic to fetch and display books
    return render(request, 'bookshelf/book_list.html', {})


