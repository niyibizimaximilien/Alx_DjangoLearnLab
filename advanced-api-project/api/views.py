from rest_framework import generics
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

# --------------------
# Author Views
# --------------------

class AuthorListView(generics.ListCreateAPIView):
    """
    GET: List all authors
    POST: Create a new author
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve an author
    PUT/PATCH: Update an author
    DELETE: Delete an author
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


# --------------------
# Book Views
# --------------------

class BookListView(generics.ListCreateAPIView):
    """
    GET: List all books
    POST: Create a new book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve a book
    PUT/PATCH: Update a book
    DELETE: Delete a book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
