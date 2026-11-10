from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer
from .serializers import UserRegisterSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class CustomTokenObtainPairView(TokenObtainPairView):
  serializer_class = CustomTokenObtainPairSerializer
  
class UserRegisterView(APIView):
  

  def post(self, request):
    serializer = UserRegisterSerializer(data=request.data)
    if serializer.is_valid():
      user = serializer.save()
      return Response(
          {
              "message": "User registered successfully.",
              "user_id": user.id,
              "username": user.username,
              "role": user.role,
          },
          status=status.HTTP_201_CREATED,
      )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)