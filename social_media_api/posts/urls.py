from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from .views import FeedViewSet
from .views import FeedView

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('feed/', FeedViewSet.as_view({'get': 'list'}), name='user_feed'),
    path('feed/', FeedView.as_view(), name='feed'),
]
