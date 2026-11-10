from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import User
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls, user):
        token= super().get_token(user)
        token['role']=user.role
        token['email']=user.email
        return token
    
    def validate(self, attrs):
        data= super().validate(attrs)
        
        data["role"] = self.user.role
        data["email"] = self.user.email
        data["username"] = self.user.username
        data["user_id"] = self.user.id
        
        return data
class UserRegisterSerializer(serializers.ModelSerializer):
  password = serializers.CharField(write_only=True)

  class Meta:
    model = User
    fields = ["id", "username", "email", "password", "role"]

  def create(self, validated_data):
    # Uses Django's secure create_user method to handle password hashing
    return User.objects.create_user(
        username=validated_data["username"],
        email=validated_data["email"],
        password=validated_data["password"],
        role=validated_data.get("role", User.Role.EMPLOYEE),
    )