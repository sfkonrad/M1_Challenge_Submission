print()
print("//// Part 3: Perform Financial Calculations \\\\\\\\")
"""
Perform financial calculations using functions.

1. Define a new function that will be used to calculate present value.
    a. This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
    b. The function should return the `present_value` for the loan.
2. Use the function to calculate the present value of the new loan given below.
    a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.
"""

# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

new_loan["annual_discount_rate"] = 0.2        # Add a key called 'annual_discount_rate' and assign it a value of 20 percent (or 0.2)

# @TODO: Define a new function that will be used to calculate present value.
#    This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#    The function should return the `present_value` for the loan.
def calculate_present_value(remaining_months, future_value, annual_discount_rate):
    present_value = future_value / (1 + (annual_discount_rate / 12)) ** remaining_months
    return(present_value)

present_value = calculate_present_value(new_loan["remaining_months"], new_loan["future_value"], new_loan["annual_discount_rate"])

# @TODO: Use the function to calculate the present value of the new loan given below.
#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.
print(f"The Present Value of this Loan is:   ${present_value: .2f}")
print()