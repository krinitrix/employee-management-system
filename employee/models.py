#employee/models.py
from django.db import models
from django.conf import settings

class Department(models.Model):
    name=models.CharField(max_length=100,unique=True)
    description=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Employee(models.Model):
    class EmploymentType(models.TextChoices):
        FULL_TIME = "FULL_TIME", "Full-Time"
        CONTRACTOR = "CONTRACTOR", "Contractor"
        INTERN = "INTERN", "Intern"

    user=models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="employee_profile",
    )
    
    department=models.ForeignKey(Department,on_delete=models.CASCADE,related_name="employees",null=True,blank=True)
    employment_type=models.CharField(choices=EmploymentType.choices,max_length=20,default=EmploymentType.FULL_TIME)
    base_salary = models.DecimalField(
      max_digits=10, decimal_places=2, default=0.00
  )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)