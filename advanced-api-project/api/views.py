from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter  # Import OrderingFilter directly
from api.models import Book
from api.serializers import BookSerializer
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)  # Use correct imports
    filterset_fields = ['title', 'author', 'publication_year']  # Filtering fields
    search_fields = ['title', 'author']  # Search functionality
    ordering_fields = ['title', 'publication_year']  # Allow ordering by title or year
    ordering = ['title']  # Default ordering


class BookListView(generics.ListAPIView):
    """Handles listing all books"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allows read-only access for unauthenticated users

class BookCreateView(generics.CreateAPIView):
    """Handles creating a new book"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Requires authentication

class BookDetailView(generics.RetrieveAPIView):
    """Handles retrieving a single book by ID"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allows read-only access for unauthenticated users

class BookUpdateView(generics.UpdateAPIView):
    """Handles updating an existing book"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Requires authentication

class BookDeleteView(generics.DestroyAPIView):
    """Handles deleting a book"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Requires authentication
