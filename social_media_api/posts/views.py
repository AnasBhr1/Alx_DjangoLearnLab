from django.shortcuts import render
from rest_framework import viewsets, permissions, filters, generics
from rest_framework import status, permissions, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Post, Comment, Like
from notifications.models import Notification  # Import Notification model
from notifications.utils import create_notification  # type: ignore # Import helper function
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .serializers import PostSerializer, CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import get_user_model
from notifications.utils import create_notification



class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only the author of a post or comment to edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        # Read-only permissions for GET, HEAD, OPTIONS requests
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions only for the owner of the object
        return obj.author == request.user

class PostViewSet(viewsets.ModelViewSet):
    """
    API view to handle CRUD operations for posts.
    """
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title', 'content']  # Allows users to search by title or content


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  # Assign the logged-in user as the author

class CommentViewSet(viewsets.ModelViewSet):
    """
    API view to handle CRUD operations for comments.
    """
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  # Assign the logged-in user as the author
        
        if Post.author != User:
            create_notification(recipient=Post.author, actor=User, verb="commented on your post", target=post)

User = get_user_model()

class UserFeedView(generics.ListAPIView):
    """
    API endpoint that returns a feed of posts from followed users.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Get the currently authenticated user
        user = self.request.user
        # Get the posts from users the current user follows, ordered by newest first
        following_users = user.following.all()  
         # Filter posts where the author is in the list of followed users, ordered by newest first
        return Post.objects.filter(author__in=following_users).order_by('-created_at')
    
class LikePostView(APIView):
    """
    API endpoint for liking and unliking a post.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        post = generics.get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        user = request.user

        if created:
            #  Create a notification when a user likes a post
            if post.author != request.user:
                Notification.objects.create(
                    recipient=post.author,   # Notify the post author
                    actor=request.user,      # The user who liked the post
                    verb="liked your post",  # Action description
                    target=post              # The liked post
                )
            return Response({"message": "Post liked successfully."}, status=status.HTTP_201_CREATED)
        else:
         return Response({"message": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)


        # Check if the user has already liked the post
        existing_like = Like.objects.filter(user=user, post=post).first()

        if existing_like:
            return Response({"message": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new like
        Like.objects.create(user=user, post=post)

        # Create a notification for the post author
        if post.author != user:
            create_notification(recipient=post.author, actor=user, verb="liked your post", target=post)

            return Response({"message": "Post liked successfully."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

class UnlikePostView(APIView):
    """
    API endpoint for unliking a post.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        post = generics.get_object_or_404(Post, pk=pk)
        like = Like.objects.filter(user=request.user, post=post)
        user = request.user

        # Find and delete the like if it exists
        like = Like.objects.filter(user=user, post=post).first()
        if like:
            like.delete()
            return Response({"message": "Post unliked successfully."}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "You have not liked this post yet."}, status=status.HTTP_400_BAD_REQUEST)