from .financial_calculator import FinancialCalculator

class MortgageCalculator(FinancialCalculator):
  
  """
  A class used to represent a mortgage calculator.

  Attributes
  -------
  months: the number of months in the loan.
  monthly_payment: the amount of the payment per month.
  """

  def __init__(self, loan_amount, annual_interest_rate, years):
    # Initialize the parent attributes and functions
    super().__init__()
    
	
    self.loan_amount = loan_amount
    
    # Initialize the monthly_interest_rate
    self.monthly_interest_rate = self.monthly_interest(annual_interest_rate)

    self.months = self.multiply(years, 12)
    self.monthly_payment = self.calculate_monthly_payment()
  
  def calculate_monthly_payment(self): 
    """
    >>> calc = MortgageCalculator(300000, 0.055, 30)
    >>> calc.monthly_payment
    1703.37 
    """
    numerator = self.monthly_interest_rate * (1 + self.monthly_interest_rate) ** self.months
    denominator = (1 + self.monthly_interest_rate) ** self.months - 1
    
    # Compute the quotient of numerator and denominator and save the result to multiplier
    multiplier = self.divide(numerator, denominator)
    
    # Calculate the monthly payment as the product of the loan amount and multiplier
    monthly_payment = round(self.multiply(self.loan_amount, multiplier), 2)
    return float(monthly_payment)
  
  

  
  
  
#mortgage_calculator = MortgageCalculator(300000, 0.055, 30)

# Use an f-string to print a message that informs the user of the monthly payment, rounded to two decimal places."
#print(f"Your monthly mortgage payment is ${round(mortgage_calculator.monthly_payment, 2)}.")


# Run doctest
#import doctest
#doctest.testmod()