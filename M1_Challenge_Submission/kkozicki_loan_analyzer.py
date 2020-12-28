# coding: utf-8
import csv
from pathlib import Path

print("Kozicki, Konrad    \\\\    Module_1_Challenge Submission    //    2020.12.27")

print("\n\\\\\\\\     Part 1: Automate the Calculations                  ////")
"""
Automate the calculations for the loan portfolio summaries.

First, let's start with some calculations on a list of prices for 5 loans.
    1. Use the `len` function to calculate the total number of loans in the list.
    2. Use the `sum` function to calculate the total of all loans in the list.
    3. Using the sum of all loans and the total number of loans, calculate the average loan price.
    4. Print all calculations with descriptive messages.
"""
loan_costs = [500, 600, 200, 1000, 450]

# How many loans are in the list?
# @TODO: Use the `len` function to calculate the total number of loans in the list.
print(f"    Total Number of Loans:                        {len(loan_costs)}")  # Prints the number of loans from the list

# What is the total of all loans?
# @TODO: Use the `sum` function to calculate the total of all loans in the list.
print(f"    Total of All Loans:                   $ {sum(loan_costs)}.00")     # Prints the total value of the loans

# What is the average loan amount from the list?
# @TODO: Using the sum of all loans and the total number of loans, calculate the average loan price.
average_loan_amount = sum(loan_costs) / len(loan_costs)
print(f"    Average Loan Amount:                  $  {average_loan_amount}0")        # Prints the average loan amount


print("\n\\\\\\\\     Part 2: Analyze Loan Data                          ////")
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
print(f"    Future Value of this Loan:            $ {loan.get('future_value')}.00")
print(f"    Remaining Term on this Loan:           {loan.get('remaining_months')} months")

# @TODO: Use the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.
#   You'll want to use the **monthly** version of the present value formula.
#   HINT: Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months

loan["discount_rate"] = 0.2        # Add a key called 'discount_rate' and assign it a value of 20 percent (or 0.2)

def present_value(loan_price, remaining_months, repayment_interval, future_value, discount_rate):
    present_value = future_value / (1 + discount_rate/12) ** remaining_months
    return present_value

present_value = present_value(loan["loan_price"], loan["remaining_months"], loan["repayment_interval"], loan["future_value"], loan["discount_rate"])

print(f"    Present Value of this Loan:           $  {round(present_value, 2)}")
loan_price = loan.get('loan_price')
print(f"    Loan Cost:                            $  {loan_price}.00")

# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# @TODO: Write a conditional statement (an if-else statement) to decide if the present value represents 
# the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says 
#       the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that 
#       the loan is too expensive and not worth the price.

if present_value >= loan_price:
    print(f"       <<<< This loan is worth{((present_value/loan_price)-1)*100: .3f}% MORE >>>>\n        <<<<  than the cost to purchase... >>>>\n            >>>>  Consider Buying It!  <<<<")
else:
    print(f"   This loan is too expensive and not worth the price. \n                    >> DO NOT BUY <<")

#print()
#print("Full Loan Details:", loan)


print("\n\\\\\\\     Part 3: Perform Financial Calculations             ////")
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

annual_discount_rate = new_loan["annual_discount_rate"] = 0.2        # Add a key called 'annual_discount_rate' and assign it a value of 20 percent (or 0.2)

# @TODO: Define a new function that will be used to calculate present value.
#    This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#    The function should return the `present_value` for the loan.
def calculate_present_value(remaining_months, future_value, annual_discount_rate):
    present_value = future_value / (1 + (annual_discount_rate / 12)) ** remaining_months
    return(present_value)

present_value = calculate_present_value(new_loan["remaining_months"], new_loan["future_value"], new_loan["annual_discount_rate"])

# @TODO: Use the function to calculate the present value of the new loan given below.
#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.
print(f"    The Present Value of this Loan is:    $ {present_value: .2f} ")

print("\n\\\\\\\\     Part 4: Conditionally filter lists of loans        ////")
"""
In this section, you will use a loop to iterate through a series of loans and select only the inexpensive 
loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to select each loan from a list of loans.
    a. Inside the for loop, write an if-statement to determine if the loan_price is less 
    than 500
    b. If the loan_price is less than 500 then append that loan to the `inexpensive_loans` list.
3. Print the list of inexpensive_loans.
"""

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

inexpensive_loans_list = []     # @TODO: Create an empty list called `inexpensive_loans`

for loan_price in loans:
    if loan_price["loan_price"] < 500:
            inexpensive_loans_list.append(loan_price)

print("   ", inexpensive_loans_list)

print("\n\\\\\\\\     Part 5: Save the results                           ////")
"""
Output this list of inexpensive loans to a csv file
    1. Use `with open` to open a new CSV file.
        a. Create a `csvwriter` using the `csv` library.
        b. Use the new csvwriter to write the header variable as the first row.
        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
            i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

    Hint: Refer to the official documentation for the csv library.
    https://docs.python.org/3/library/csv.html#writer-objects

"""
# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# @TODO: Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
print("     Writing the data to a CSV file...")
# Open the output CSV file path using `with open`
with open(output_path, "w") as csvfile:
    # Create a csvwriter
    csvwriter = csv.writer(csvfile, delimiter=",")

    # Write the header to the CSV file
    csvwriter.writerow(header)

    # Write the values of each dictionary inside of `inexpensive_loans_list`
    # as a row in the CSV file.
    for item in inexpensive_loans_list:
        csvwriter.writerow(item.values())
print("\n          <>  Success! Data has been written from  <>\n          <> new list(s) to the specified CSV file <>")





print("\n\n            {end of the loan_analyzer.py program}\n")