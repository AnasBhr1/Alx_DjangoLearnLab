from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from api.models import Book
from api.serializers import BookSerializer

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
