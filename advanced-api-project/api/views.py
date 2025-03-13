from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListCreateAPIView):
    """Handles listing all books and creating a new book."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Handles retrieving, updating, and deleting a single book by ID."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
