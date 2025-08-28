import pytest
from app.calculators.basic_calculator import BasicCalculator
from app.calculators.financial_calculator import FinancialCalculator
from app.calculators.loan_calculator import LoanCalculator
from app.calculators.mortgage_calculator import MortgageCalculator

def test_basic_calculator_add():
    calc = BasicCalculator()
    assert calc.add(5, 3) == 8

def test_financial_calculator_monthly_interest():
    calc = FinancialCalculator()
    assert calc.monthly_interest(0.06) == pytest.approx(0.005, 0.0001)

def test_mortgage_calculator_example():
    calc = MortgageCalculator(200000, 0.065, 30)
    assert calc.calculate_monthly_payment() == pytest.approx(1264.14, 0.01)

def test_loan_calculator_example():
    calc = LoanCalculator(179.87, 0.06, 30)
    assert calc.calculate_loan_amount() == pytest.approx(30000.81, 0.01)