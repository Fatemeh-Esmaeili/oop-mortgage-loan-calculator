# Relative import
from .basic_calculator import BasicCalculator

class FinancialCalculator(BasicCalculator):    
    
    def monthly_interest(self, annual_interest_rate:float) -> float:
        '''
        >>> calc = FinancialCalculator()
        >>> calc.monthly_interest(0.06)
        0.005
        '''
        return float(self.divide(annual_interest_rate, 12))

    def months_from_years(self, years):
        '''
        >>> calc = FinancialCalculator()
        >>> calc.months_from_years(2)
        24.0
        '''
        return float(self.multiply(years, 12))
    

# Run doctest
#import doctest
#doctest.testmod()