from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from api.models import Book

class BookAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="password")
        self.client.force_authenticate(user=self.user)

        self.book1 = Book.objects.create(title="Django for Beginners", author="William S.", publication_year=2021)
        self.book2 = Book.objects.create(title="REST APIs with Django", author="John Doe", publication_year=2022)

        self.valid_book_data = {"title": "New Book", "author": "Author Name", "publication_year": 2023}
        self.invalid_book_data = {"title": "", "author": "Author Name", "publication_year": 2023}

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
git add .
git commit -m "Added unit tests for API endpoints"
git push origin main
