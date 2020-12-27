# coding: utf-8
import csv
from pathlib import Path

print("Kozicki, Konrad    //    Module_1_Challenge Submission    //    2020.12.27")
print() # additional line spacing for aesthetic purposes


print("////Part 1: Automate the Calculations\\\\\\\\")
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
print(f"Total Number of Loans:          {len(loan_costs)}")  # Prints the number of loans from the list

# What is the total of all loans?
# @TODO: Use the `sum` function to calculate the total of all loans in the list.
print(f"Total of All Loans:      ${sum(loan_costs)}.00")     # Prints the total value of the loans

# What is the average loan amount from the list?
# @TODO: Using the sum of all loans and the total number of loans, calculate the average loan price.
average_loan_amount = sum(loan_costs) / len(loan_costs)
print(f"Average Loan Amount:     $ {average_loan_amount}0")        # Prints the average loan amount