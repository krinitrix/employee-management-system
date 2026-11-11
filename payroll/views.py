from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Payroll
from .serializers import PayrollSerializer
from users.permissions import IsHRAdmin


class PayrollListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsHRAdmin]
    queryset = Payroll.objects.select_related(
        "employee", "employee__user", "employee__department"
    )
    serializer_class = PayrollSerializer


class MyPayrollListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PayrollSerializer

    def get_queryset(self):
        return Payroll.objects.filter(
            employee__user=self.request.user
        ).select_related(
            "employee",
            "employee__user",
            "employee__department"
        )
