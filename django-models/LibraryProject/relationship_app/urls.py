from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    # URL pattern for the function-based view that lists all books
    path('books/', list_books, name='list_books'),

    # URL pattern for the class-based view that displays library details
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
