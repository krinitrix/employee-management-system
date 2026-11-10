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
