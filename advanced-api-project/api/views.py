from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from api.models import Book
from api.serializers import BookSerializer

class BookListView(generics.ListCreateAPIView):
    """Handles listing all books and creating a new book"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Handles retrieving, updating, and deleting a single book"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
