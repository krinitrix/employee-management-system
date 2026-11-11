#employee/views.py
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
from django.db import transaction
from .serializers import EmployeeProfileSerializer,EmployeeCreateSerializer,EmployeeUpdateSerializer,DepartmentSerializer
from users.models import User
from users.permissions import IsHRAdmin
from rest_framework.permissions import IsAuthenticated
from .models import Employee,Department
from django.shortcuts import get_object_or_404

class EmployeeListCreateView(generics.ListCreateAPIView):
  permission_classes = [IsAuthenticated, IsHRAdmin]
  queryset = Employee.objects.all().select_related("user", "department")

  def get_serializer_class(self):
    
    if self.request.method == "POST":
      return EmployeeCreateSerializer
    return EmployeeProfileSerializer


  def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    
    employee = serializer.save()  

    response_serializer = EmployeeProfileSerializer(employee)
    return Response(
        {
            "message": "Employee profile created successfully.",
            "data": response_serializer.data,
        },
        status=status.HTTP_201_CREATED,
    )
    
class EmployeeDetailUpdateView(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = [IsAuthenticated, IsHRAdmin]
  queryset = Employee.objects.all()
  serializer_class = (
      EmployeeProfileSerializer  
  )
  def perform_destroy(self, instance):
        instance.user.delete()
        

  def get_serializer_class(self):
    
    if self.request.method in ["PUT", "PATCH"]:
      return EmployeeUpdateSerializer
    return EmployeeProfileSerializer


class DepartmentListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsHRAdmin]
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsHRAdmin]
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    

class MyEmployeeProfileView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EmployeeProfileSerializer

    def get_object(self):
        return get_object_or_404(
            Employee.objects.select_related("user", "department"),
            user=self.request.user
        )