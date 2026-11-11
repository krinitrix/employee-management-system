
from decimal import Decimal

from rest_framework import serializers
from employee.models import Employee
from .models import Payroll


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

        basic_salary = employee.base_salary
        allowances = attrs.get("allowances", Decimal("0.00"))
        deductions = attrs.get("deductions", Decimal("0.00"))

        gross_salary = basic_salary + allowances

        if deductions > gross_salary:
            raise serializers.ValidationError(
                "Deductions cannot exceed gross salary."
            )

        return attrs

    def create(self, validated_data):
        employee = validated_data["employee"]

        basic_salary = employee.base_salary
        allowances = validated_data.get("allowances", Decimal("0.00"))
        deductions = validated_data.get("deductions", Decimal("0.00"))

        gross_salary = basic_salary + allowances
        net_salary = gross_salary - deductions

        validated_data["basic_salary"] = basic_salary
        validated_data["gross_salary"] = gross_salary
        validated_data["net_salary"] = net_salary

        return Payroll.objects.create(**validated_data)
