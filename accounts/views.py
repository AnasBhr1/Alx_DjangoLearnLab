from rest_framework.views import APIView
from rest_framework.response import Response

class RegisterView(APIView):
    def post(self, request):
        return Response({"message": "User registered successfully"})

class LoginView(APIView):
    def post(self, request):
        return Response({"message": "User logged in successfully"})

class ProfileView(APIView):
    def get(self, request):
        return Response({"message": "User profile data"})
