

def main():
    loanAmount = getValidLoanAmount()
    annualInterestRate = float(input("Enter annual interest rate (as a percentage): ")) / 100
    loanTermYears = int(input("Enter loan term in years: "))
    monthlyPayment = calculateMonthlyPayment(loanAmount, annualInterestRate, loanTermYears)
    displayPaymentCalculatorResult(loanAmount, annualInterestRate, loanTermYears, monthlyPayment)

def displayPaymentCalculatorResult(loan, annualRate, termYears, payment):
    print(f"{'Loan Amount':15}: ${loan:,.2f}")
    print(f"{'Term':15}: {termYears:,} year(s)")
    print(f"{'Rate':15}: {annualRate * 100:,.1f}%")
    print(f"{'Payment':15}: ${payment:,.2f}")

def calculateMonthlyPayment(loan_amount, annual_interest_rate, loan_term_years):
    """Calculates the monthly payment given loan details."""

    monthly_interest_rate = annual_interest_rate / 12
    number_of_payments = loan_term_years * 12

    payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments) / \
              ((1 + monthly_interest_rate) ** number_of_payments - 1)

    return payment

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


main()
