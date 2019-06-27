"""
Write a program to calculate the credit card balance after one year if a
person only pays the minimum monthly payment required by the credit card
company each month. The following variables contain values as described
below:

balance = the outstanding balance on the credit card
annualInterestRate = annual interest rate as a decimal
monthlyPaymentRate = minimum monthly payment rate as a decimal
"""
for month in range (1, 13):
    balance *= 1 - monthlyPaymentRate
    balance += annualInterestRate/12 * balance
print("Remaining balance: " + str(round(balance, 2)))
