from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # Import the views file
from .views import list_books, LibraryDetailView, user_login, user_logout, register

urlpatterns = [
    # URL pattern for the function-based view that lists all books
    path('books/', list_books, name='list_books'),

    # URL pattern for the class-based view that displays library details
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]
]
