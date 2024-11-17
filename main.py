# ##############################################################################
#  Written by: Evan McDaniel, Khalid Elmounaichet, and Pedro Moran             #
#  Date Written: 11-17-2024                                                    #
#  Purpose: The purpose of the following source code is to create a calculator #
#  for a loan between 1 and 100,000.                                           #
# ##############################################################################

# Main function responsible for holding the main flow of the program
def main():
    loanAmount = getValidLoanAmount()
    annualInterestRate = float(input("Enter annual interest rate (as a percentage): "))
    loanTermYears = int(input("Enter loan term in years: "))
    monthlyPayment = calculateMonthlyPayment(loanAmount, annualInterestRate, loanTermYears)
    displayPaymentCalculatorResult(loanAmount, annualInterestRate, loanTermYears, monthlyPayment)

# Function that displays the details of the calculator
def displayPaymentCalculatorResult(loan, annualRate, termYears, payment):
    print(f"{'Loan Amount':15}: ${loan:,.2f}")
    print(f"{'Term':15}: {termYears:,} year(s)")
    print(f"{'Rate':15}: {annualRate:,.1f}%")
    print(f"{'Payment':15}: ${payment:,.2f}")

# Function that calculates the monthly payment given loan details.
def calculateMonthlyPayment(loanAmount, annualInterestRate, loanTermYears):
    """Calculates the monthly payment given loan details."""

    monthly_interest_rate = (annualInterestRate / 100) / 12
    number_of_payments = loanTermYears * 12

    payment = loanAmount * ((monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments) /
                            ((1 + monthly_interest_rate) ** number_of_payments - 1))

    return payment

# Function that validates and return a loan between 1 and 100,000.
def getValidLoanAmount():
    while True:
        try:
            loan_amount = float(input("Enter loan amount ( greater than 0 and less or equal to 100000):"))
            if 0 < loan_amount <= 100000:
                return loan_amount
            else:
                print("Invalid loan amount. Please enter a value between 0 and 100000.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Call to the main function
main()
