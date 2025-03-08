#from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
# Create your views here.
class BookList(ListAPIView):
    queryset = Book.objects.all() #to retrieve all books from the db
    serializer_class = BookSerializer # use bookserializer to format data

class BookViewSet(viewsets.ModelViewSet): # view set to CRUD operations
    queryset = Book.objects.all() #to retrieve all books
    serializer_class = BookSerializer #to format data using book serializer

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class CustomAuthToken(ObtainAuthToken):
     def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user_id': user.id, 'username': user.username})