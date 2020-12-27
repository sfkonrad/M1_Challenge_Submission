print()
print("////Part 2: Analyze Loan Data\\\\\\\\")
"""
Analyze the loan to determine the investment evaluation.

Using more detailed data on one of these loans, follow these steps to calculate a Present Value, or 
a "fair price" for what this loan would be worth.

1. Use get() on the dictionary of additional information to extract the **Future Value** 
    and **Remaining Months** on the loan.
    a. Save these values as variables called `future_value` and `remaining_months`.
    b. Print each variable.

    @NOTE:
    **Future Value**: The amount of money the borrower has to pay back upon maturity of the 
    loan (a.k.a. "Face Value")
    **Remaining Months**: The remaining maturity (in months) before the loan needs to be fully repaid.

2. Use the formula for Present Value to calculate a "fair value" of the loan. Use a minimum required 
    return of 20% as the discount rate.
3. Write a conditional statement (an if-else statement) to decide if the present value represents the 
    loan's fair value.
    a. If the present value of the loan is greater than or equal to the cost, then print a message that 
    says the loan is worth at least the cost to buy it.
    b. Else, the present value of the loan is less than the loan cost, then print a message that says that 
    the loan is too expensive and not worth the price.

    @NOTE:
    If Present Value represents the loan's fair value (given the required minimum return of 20%), does it 
    make sense to buy the loan at its current cost?
"""
# Given the following loan data, you will need to calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Use get() on the dictionary of additional information to extract the Future Value 
# and Remaining Months on the loan.
print(f"Future Value of this Loan:            $ {loan.get('future_value')}.00")
print(f"Remaining Term on this Loan:                  {loan.get('remaining_months')} months")

# @TODO: Use the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.
#   You'll want to use the **monthly** version of the present value formula.
#   HINT: Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months

loan["discount_rate"] = 0.2        # Add a key called 'discount_rate' and assign it a value of 20 percent (or 0.2)

def present_value(loan_price, remaining_months, repayment_interval, future_value, discount_rate):
    present_value = future_value / (1 + discount_rate/12) ** remaining_months
    return present_value

fair_value = present_value(loan["loan_price"], loan["remaining_months"], loan["repayment_interval"], loan["future_value"], loan["discount_rate"])

print(f"Present 'Fair Value' of this Loan:    $  {round(fair_value, 2)}")
print()

# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# @TODO: Write a conditional statement (an if-else statement) to decide if the present value represents 
# the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says 
#       the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that 
#       the loan is too expensive and not worth the price.
# YOUR CODE HERE!



print("Full Loan Details:", loan)