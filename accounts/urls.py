from django.urls import path
from .views import (
    UserRegistrationView,
    UserLoginView,
    UserProfileView
)

urlpatterns = [
    # User registration endpoint
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    
    # User login endpoint
    path('login/', UserLoginView.as_view(), name='user-login'),
    
    # User profile management endpoint
    path('profile/', UserProfileView.as_view(), name='user-profile'),
]