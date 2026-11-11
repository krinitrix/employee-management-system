#payroll/services.py
from decimal import Decimal


def calculate_payroll(basic_salary, allowances, deductions):
    """
    Calculate gross salary and net salary.

    Business rules:
    - Salary components cannot be negative.
    - Deductions cannot exceed gross salary.
    """

    if basic_salary < 0:
        raise ValueError("Basic salary cannot be negative.")

    if allowances < 0:
        raise ValueError("Allowances cannot be negative.")

    if deductions < 0:
        raise ValueError("Deductions cannot be negative.")

    gross_salary = basic_salary + allowances

    if deductions > gross_salary:
        raise ValueError(
            "Deductions cannot exceed gross salary."
        )

    net_salary = gross_salary - deductions

    return {
        "basic_salary": basic_salary,
        "gross_salary": gross_salary,
        "net_salary": net_salary
    }
