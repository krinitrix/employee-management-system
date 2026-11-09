from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    
    class Role(models.TextChoices):
        HR_ADMIN = "HR_ADMIN", "HR Administrator"
        EMPLOYEE = "EMPLOYEE", "Employee"
    
    role=models.CharField(choices=Role.choices,default=Role.EMPLOYEE,max_length=50)
    email=models.EmailField(unique=True)
    
  
    
    def __str__(self):
        return f"{self.email} ({self.role})"