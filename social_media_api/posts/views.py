from rest_framework import generics, permissions
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post, Like
from rest_framework.exceptions import NotFound
from django.contrib.contenttypes.models import ContentType
from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from notifications.models import Notification  
from rest_framework.permissions import IsAuthenticated

User = get_user_model()

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at']

# Feed View: Retrieve posts from followed users
class FeedView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        following_users = user.following.all()  # Get the users that the current user follows

        # Get posts from users the current user follows
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

        # Serialize posts
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
# class LikePostView(generics.GenericAPIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def post(self, request, pk):
#         user = request.user
#         try:
#             post = Post.objects.get(pk=pk)
#         except Post.DoesNotExist:
#             raise NotFound("Post not found")

#         # Prevent user from liking the post again
#         if Like.objects.filter(user=user, post=post).exists():
#             return Response({"message": "You have already liked this post."}, status=400)

#         # Create Like
#         like = Like.objects.create(user=user, post=post)

#         # Create a notification for the post's author
#         notification = Notification.objects.create(
#             recipient=post.author,
#             actor=user,
#             verb="liked your post",
#             target_content_type=ContentType.objects.get_for_model(Post),
#             target_object_id=post.id,
#         )

#         return Response({"message": "Post liked successfully."}, status=201)

# class UnlikePostView(generics.GenericAPIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def post(self, request, pk):
#         user = request.user
#         try:
#             post = Post.objects.get(pk=pk)
#         except Post.DoesNotExist:
#             raise NotFound("Post not found")

#         # Check if the post is liked
#         like = Like.objects.filter(user=user, post=post).first()
#         if not like:
#             return Response({"message": "You have not liked this post."}, status=400)

#         # Delete Like
#         like.delete()

#         return Response({"message": "Post unliked successfully."}, status=200)

class LikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)  # Get the post or 404 if not found
        # Get or create a like for the post by the current user
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if created:
            # Create a notification for the user whose post was liked
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked",
                target=post
            )
            return Response({"message": "Post liked."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "You already liked this post."}, status=status.HTTP_400_BAD_REQUEST)


class UnlikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)  # Get the post or 404 if not found
        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()  # Remove the like
            return Response({"message": "Post unliked."}, status=status.HTTP_204_NO_CONTENT)
        except Like.DoesNotExist:
            return Response({"message": "You haven't liked this post yet."}, status=status.HTTP_400_BAD_REQUEST)
    
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()  # Get all posts
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  # Assign the post to the current logged-in user

    def get_queryset(self):
        """This will return posts for the logged-in user only"""
        return Post.objects.filter(author=self.request.user)

# Comment ViewSet
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()  # Get all comments
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  # Assign the comment to the current logged-in user

    def get_queryset(self):
        """This will return comments for posts created by the logged-in user"""
        return Comment.objects.filter(post__author=self.request.user)