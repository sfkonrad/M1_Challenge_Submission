print("\n \\\\\\\\      Part 4: Conditionally filter lists of loans                 ////")
"""
In this section, you will use a loop to iterate through a series of loans and select only the inexpensive 
loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to select each loan from a list of loans.
    a. Inside the for loop, write an if-statement to determine if the loan_price is less than 500
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

print(loans)
print("\n \n")

# @TODO: Create an empty list called `inexpensive_loans`
loan_price = loans("loan_price")
inexpensive_loans = []

# @TODO: Loop through all the loans and append any that cost $500 or less to the 
# `inexpensive_loans` list
for key in loans:
    if loans[loan_price] <= 500:
        inexpensive_loans.append(loans[key])

# @TODO: Print the `inexpensive_loans` list
print(inexpensive_loans)