from django.urls import path
from .views import list_books, LibraryDetailView, user_login, user_logout, register

urlpatterns = [
    # URL pattern for the function-based view that lists all books
    path('books/', list_books, name='list_books'),

    # URL pattern for the class-based view that displays library details
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
]
