from decimal import Decimal
import pytest

from payroll.services import calculate_payroll


def test_successful_payroll_calculation():
    result = calculate_payroll(
        Decimal("25000.00"),
        Decimal("2000.00"),
        Decimal("500.00")
    )

    assert result["basic_salary"] == Decimal("25000.00")
    assert result["gross_salary"] == Decimal("27000.00")
    assert result["net_salary"] == Decimal("26500.00")


def test_negative_basic_salary():
    with pytest.raises(ValueError):
        calculate_payroll(
            Decimal("-1000.00"),
            Decimal("0.00"),
            Decimal("0.00")
        )
        

def test_negative_allowances():
    with pytest.raises(
        ValueError, match="Allowances cannot be negative."
    ):
        calculate_payroll(
            Decimal("25000.00"),
            Decimal("-500.00"),
            Decimal("0.00")
        )


def test_negative_deductions():
    with pytest.raises(
        ValueError, match="Deductions cannot be negative."
    ):
        calculate_payroll(
            Decimal("25000.00"),
            Decimal("0.00"),
            Decimal("-500.00")
        )


def test_deductions_exceed_gross_salary():
    with pytest.raises(
        ValueError,
        match="Deductions cannot exceed gross salary."
    ):
        calculate_payroll(
            Decimal("25000.00"),
            Decimal("2000.00"),
            Decimal("28000.00")
        )
