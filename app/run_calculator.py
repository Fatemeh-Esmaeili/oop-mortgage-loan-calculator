def main():
    from app.calculators.mortgage_calculator import MortgageCalculator
    from app.calculators.loan_calculator import LoanCalculator

    
    print("Welcome to the Mortgage & Loan Calculator!")

    while True:
        print("\nOptions:")
        print("1 - Calculate monthly mortgage payment")
        print("2 - Calculate loan amount from monthly payment")
        print("Q - Quit")


        choice = input("Choose an option (1/2/Q): ").strip().upper()

        if choice == '1':
            try:
                loan_amount = float(input("Enter the loan amount: "))
                annual_interest_rate = float(input("Enter the annual interest rate (as a decimal): "))
                years = int(input("Enter the number of years for the loan: "))

                mortgage_calculator = MortgageCalculator(loan_amount, annual_interest_rate, years)
                print(f"Your monthly mortgage payment of ${mortgage_calculator.loan_amount} loan is ${round(mortgage_calculator.monthly_payment, 2)}.")
            except ValueError:
                print("Invalid input! Please enter numeric values.")

        elif choice == '2':
            # Loan amount from monthly payment
            try:
                monthly_payment = float(input("Enter the monthly payment: "))
                annual_interest_rate = float(input("Enter the annual interest rate (as a decimal): "))
                years = int(input("Enter the number of years for the loan: "))

                loan_calculator = LoanCalculator(monthly_payment, annual_interest_rate, years)        
                print(f"The loan amount for a monthly payment of ${loan_calculator.monthly_payment} is ${round(loan_calculator.loan_amount, 2)}.")
            except ValueError:
                print("Invalid input! Please enter numeric values.")

        elif choice == 'Q':
            print("Thank you for using the calculator. Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1, 2, or Q.")


if __name__ == "__main__":
    main()