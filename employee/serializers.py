

from rest_framework import serializers
from .models import Department, Employee
from users.models import User

class DepartmentSerializer(serializers.ModelSerializer):

  class Meta:
    model = Department
    fields = ["id", "name", "description", "created_at"]


# Serializer used for reading/listing employees (GET)
class EmployeeProfileSerializer(serializers.ModelSerializer):
  department = DepartmentSerializer(read_only=True)
  email = serializers.EmailField(source="user.email", read_only=True)
  username = serializers.CharField(source="user.username", read_only=True)
  role = serializers.CharField(source="user.role", read_only=True)

  class Meta:
    model = Employee
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


# Serializer used specifically for validating incoming POST data
class UserNestedCreateSerializer(serializers.Serializer):
  username = serializers.CharField(max_length=150)
  email = serializers.EmailField()
  password = serializers.CharField(write_only=True)
  role = serializers.ChoiceField(
      choices=User.Role.choices, default=User.Role.EMPLOYEE
  )


class EmployeeCreateSerializer(serializers.Serializer):
  user = UserNestedCreateSerializer()
  department_id = serializers.IntegerField(required=False, allow_null=True)
  employment_type = serializers.CharField(required=False, default="FULL_TIME")
  base_salary = serializers.DecimalField(
      max_digits=10, decimal_places=2, default=0.00
  )

  def validate_department_id(self, value):
    if value and not Department.objects.filter(id=value).exists():
      raise serializers.ValidationError("Department with this ID does not exist.")
    return value