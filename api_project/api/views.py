from rest_framework import generics 
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import YourModel
from .serializers import YourModelSerializer


class BookList(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()  # This will retrieve all books from the database

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Restrict access to authenticated users
