from fastapi import FastAPI
from app.calculators.mortgage_calculator import MortgageCalculator
from app.calculators.loan_calculator import LoanCalculator

application = FastAPI(title="Mortgage Calculator API")

@application.get("/mortgage_payment")
def calculate_mortgage(loan_amount: float, annual_interest_rate: float, years: int):
    calc = MortgageCalculator(loan_amount, annual_interest_rate, years)
    return {"monthly_payment": round(calc.monthly_payment, 2)}

@application.get("/loan_amount")
def calculate_loan(monthly_payment: float, annual_interest_rate: float, years: int):
    calc = LoanCalculator(monthly_payment, annual_interest_rate, years)
    return {"loan_amount": round(calc.loan_amount, 2)}


# To run the application, use the command:
# uvicorn app.main:application --reload