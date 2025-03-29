from django.urls import path
<<<<<<< HEAD
from .views import RegisterView, LoginView, ProfileView
=======
from .views import RegisterView, LoginView, UserProfileView
>>>>>>> 81ca2c6 (Initial commit to sync with GitHub)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
<<<<<<< HEAD
    path('profile/', ProfileView.as_view(), name='profile'),
=======
    path('profile/', UserProfileView.as_view(), name='profile'),
>>>>>>> 81ca2c6 (Initial commit to sync with GitHub)
]
