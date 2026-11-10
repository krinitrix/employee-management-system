from rest_framework import serializers
from .models import Department, EmployeeProfile


class DepartmentSerializer(serializers.ModelSerializer):

  class Meta:
    model = Department
    fields = ["id", "name", "description", "created_at"]


class EmployeeProfileSerializer(serializers.ModelSerializer):
  
  department = DepartmentSerializer(read_only=True)
  email = serializers.EmailField(source="user.email", read_only=True)
  username = serializers.CharField(source="user.username", read_only=True)
  role = serializers.CharField(source="user.role", read_only=True)

  class Meta:
    model = EmployeeProfile
    fields = [
        "id",
        "username",
        "email",
        "role",
        "department",
        "employment_type",
        "base_salary",
        "created_at",
    ]