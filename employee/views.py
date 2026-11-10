#employee/views.py
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from .serializers import EmployeeProfileSerializer,EmployeeCreateSerializer
from users.models import User
from users.permissions import IsHRAdmin
from rest_framework.permissions import IsAuthenticated
from .models import Employee,Department


class EmployeeCreateView(APIView):
    permission_classes = [IsAuthenticated, IsHRAdmin]

    @transaction.atomic
    def post(self, request):
        # 1. Validate request
        serializer = EmployeeCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        user_data = validated_data.pop("user")
        department_id = validated_data.pop("department_id", None)

        user = User.objects.create_user(
        username=user_data["username"],
        email=user_data["email"],
        password=user_data["password"],
        role=user_data.get("role"),)
        
        
        department = None
        if department_id :
            department = Department.objects.get(id=department_id)
        
        employee = Employee.objects.create(
        user=user,
        department=department,
        employment_type=validated_data.get("employment_type", "FULL_TIME"),
        base_salary=validated_data.get("base_salary", 0.00),
    )
        
        response_serializer =EmployeeProfileSerializer(employee)
        return Response(
        {
            "message": "Employee profile created.",
            "data": response_serializer.data,
        },
        status=status.HTTP_201_CREATED,
    )
    