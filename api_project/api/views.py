from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

# old list view (still works if you want a read-only endpoint)
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# new CRUD ViewSet
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
