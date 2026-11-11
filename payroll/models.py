
from django.db import models
from employee.models import Employee


class Payroll(models.Model):

    class Status(models.TextChoices):
        DRAFT = "DRAFT", "Draft"
        PROCESSED = "PROCESSED", "Processed"
        PAID = "PAID", "Paid"

    employee = models.ForeignKey(
        Employee,
        on_delete=models.PROTECT,
        related_name="payroll_records"
    )

    month = models.PositiveSmallIntegerField()
    year = models.PositiveSmallIntegerField()

    basic_salary = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    allowances = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    deductions = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    gross_salary = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    net_salary = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.DRAFT
    )

    created_at = models.DateTimeField(auto_now_add=True)
    paid_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["employee", "month", "year"],
                name="unique_employee_payroll_period"
            )
        ]
        ordering = ["-year", "-month"]

    def __str__(self):
        return f"{self.employee} - {self.month}/{self.year}"
