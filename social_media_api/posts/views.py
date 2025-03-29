from rest_framework import generics, permissions
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .models import Post
from rest_framework import serializers
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Post, Like
from .serializers import PostSerializer
from rest_framework.exceptions import NotFound
from django.contrib.auth import get_user_model
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType

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
    
class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        user = request.user
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise NotFound("Post not found")

        # Prevent user from liking the post again
        if Like.objects.filter(user=user, post=post).exists():
            return Response({"message": "You have already liked this post."}, status=400)

        # Create Like
        like = Like.objects.create(user=user, post=post)

        # Create a notification for the post's author
        notification = Notification.objects.create(
            recipient=post.author,
            actor=user,
            verb="liked your post",
            target_content_type=ContentType.objects.get_for_model(Post),
            target_object_id=post.id,
        )

        return Response({"message": "Post liked successfully."}, status=201)

class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        user = request.user
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise NotFound("Post not found")

        # Check if the post is liked
        like = Like.objects.filter(user=user, post=post).first()
        if not like:
            return Response({"message": "You have not liked this post."}, status=400)

        # Delete Like
        like.delete()

        return Response({"message": "Post unliked successfully."}, status=200)