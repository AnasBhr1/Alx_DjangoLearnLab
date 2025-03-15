from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from api.models import Book
from rest_framework.test import APITestCase

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')  # Ensure login before requests
        self.book = Book.objects.create(title="Test Book", author="Author", publication_year=2022)

    def test_authenticated_book_creation(self):
        response = self.client.post('/api/books/', {'title': 'New Book', 'author': 'Someone', 'publication_year': 2023})
        self.assertEqual(response.status_code, 201)  # Ensure creation works

    def test_list_books(self):
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_valid_book(self):
        response = self.client.post("/api/books/", self.valid_book_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_create_invalid_book(self):
        response = self.client.post("/api/books/", self.invalid_book_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_book(self):
        update_data = {"title": "Updated Title", "author": "Updated Author", "publication_year": 2024}
        response = self.client.put(f"/api/books/{self.book1.id}/", update_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        response = self.client.delete(f"/api/books/{self.book1.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
