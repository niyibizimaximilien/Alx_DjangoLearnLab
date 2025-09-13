from .forms import ExampleForm
from django.shortcuts import render
from .models import Book
from django.contrib.auth.decorators import permission_required


# List all books (requires can_view permission)
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()  # fetch all books
    return render(request, "bookshelf/book_list.html", {"books": books})

