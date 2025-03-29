from django.shortcuts import render
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer, LoginSerializer
from django.contrib.auth import authenticate
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

# class RegisterView(views.APIView):
#     def post(self, request):
#         serializer = RegisterSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             return Response({'user': RegisterSerializer(user).data}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class LoginView(views.APIView):
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         if serializer.is_valid():
#             user = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
#             if user:
#                 token, created = Token.objects.get_or_create(user=user)
#                 return Response({'token': token.key})
#             return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

User = get_user_model()

# Follow User View
class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(User, id=user_id)
        user = request.user

        # Prevent following oneself
        if user == user_to_follow:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        # Add user to the following list
        user.following.add(user_to_follow)
        return Response({"detail": f"Followed {user_to_follow.username}."}, status=status.HTTP_200_OK)

# Unfollow User View
class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(User, id=user_id)
        user = request.user

        # Prevent unfollowing oneself
        if user == user_to_unfollow:
            return Response({"detail": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        # Remove user from the following list
        user.following.remove(user_to_unfollow)
        return Response({"detail": f"Unfollowed {user_to_unfollow.username}."}, status=status.HTTP_200_OK)