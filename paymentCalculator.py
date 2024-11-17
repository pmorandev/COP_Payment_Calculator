'''######################################################################
##  Written by......: khalid elmounaichet                             ###
##  Date Written....: Nov 7, 2024                                     ###
## Purpose..........: Demonstrate the monthly  payment calculator     ###
#########################################################################
'''
###################################################################################

def get_valid_loan_amount():
        while True:
            try:

                loan_amount = float(input("Enter loan amount ( greater than 0 and less or equal to 100000):"))

                if 0 < loan_amount <= 100000:
                     return loan_amount
                else:
                     print("Invalid loan amount. Please enter a value between 0 and 100000.")
            except ValueError:

                print("Invalid input. Please enter a number.")
def main():


 loan = get_valid_loan_amount()
 print("Valid loan amount:", loan)

main()
##############################################################################################

def main():
    """Calculates and prints the monthly payment for a loan ."""

    loan_amount = float (input("Enter loan amount: "))
    annual_interest_rate = float(input("Enter annual interest rate (as a percentage): ")) / 100
    loan_term_years = int( input("Enter loan term in years: "))

    monthly_payment = calculate_monthly_payment(loan_amount, annual_interest_rate, loan_term_years)

    print(f"Monthly payment: ${monthly_payment:.2f}")

def calculate_monthly_payment(loan_amount, annual_interest_rate, loan_term_years):
    """Calculates the monthly payment given loan details."""

    monthly_interest_rate = annual_interest_rate / 12
    number_of_payments = loan_term_years * 12

    payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments) / \
              ((1 + monthly_interest_rate) ** number_of_payments - 1)

    return payment

main()






