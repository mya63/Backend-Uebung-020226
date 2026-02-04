from django.contrib.auth import authenticate
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer

class RegisterView(generics.CreateAPIView):
  serializer_class = RegisterSerializer
  permission_classes = [permissions.AllowAny]

class LoginView(generics.GenericAPIView):
  permission_classes = [permissions.AllowAny]

  def post(self, request):
      username = request.data.get("username")
      password = request.data.get("password")

      user = authenticate(username=username, password=password)
      if not user: 
         return Response({"detail": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        
      token, _ = Token.objects.get_or_create(user=user)
      return Response({"token": token.key, "user_id": user.id, "username": user.username})