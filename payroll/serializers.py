
from decimal import Decimal

from rest_framework import serializers
from employee.models import Employee
from .models import Payroll
from .services import calculate_payroll

class PayrollSerializer(serializers.ModelSerializer):

    employee = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all()
    )

    month = serializers.IntegerField(min_value=1, max_value=12)
    year = serializers.IntegerField(min_value=2000, max_value=9999)

    allowances = serializers.DecimalField(
        max_digits=12,
        decimal_places=2,
        required=False,
        default=Decimal("0.00"),
        min_value=Decimal("0.00")
    )

    deductions = serializers.DecimalField(
        max_digits=12,
        decimal_places=2,
        required=False,
        default=Decimal("0.00"),
        min_value=Decimal("0.00")
    )

    class Meta:
        model = Payroll
        fields = "__all__"
        read_only_fields = [
            "basic_salary",
            "gross_salary",
            "net_salary",
            "status",
            "created_at",
            "paid_at"
        ]

    def validate(self, attrs):
        employee = attrs["employee"]

        allowances = attrs.get("allowances", Decimal("0.00"))
        deductions = attrs.get("deductions", Decimal("0.00"))

        try:
            calculated_values = calculate_payroll(
                basic_salary=employee.base_salary,
                allowances=allowances,
                deductions=deductions
            )

        except ValueError as exc:
            raise serializers.ValidationError(str(exc))

        attrs.update(calculated_values)

        return attrs
