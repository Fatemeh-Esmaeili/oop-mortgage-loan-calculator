
from .financial_calculator import FinancialCalculator

class LoanCalculator(FinancialCalculator):
  
  """
  A class used to represent a loan calculator.

  Attributes
  -------
  loan_amount: the loan amount calculated from monthly payment, monthly interest rate, and total number of payments.  
  """
  def __init__(self, monthly_payment, annual_interest_rate, years):
        # Initialize the parent attributes and functions
        super().__init__()
        self.monthly_payment = monthly_payment  
        self.monthly_interest_rate = self.divide(annual_interest_rate, 12) 
        self.nbr_payments = self.multiply(years, 12)
        self.loan_amount = self.calculate_loan_amount()    
    
  def calculate_loan_amount(self):    
        """
        Calculate the loan amount based on monthly payment, monthly interest rate, and total number of payments.
        """   
        # Raise an error if the number of total payment is less than zero
        if self.nbr_payments <= 0:
            raise ValueError("The number of payments must be greater than zero.")

        loan_amount = (self.monthly_payment * ((1 + self.monthly_interest_rate) ** self.nbr_payments - 1)) / \
                      (self.monthly_interest_rate * (1 + self.monthly_interest_rate) ** self.nbr_payments)
        
        loan_amount = round(loan_amount, 2)
        # Return the loan amount
        return loan_amount
        