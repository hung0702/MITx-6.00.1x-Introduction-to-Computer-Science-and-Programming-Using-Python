"""
Now write a program that calculates the minimum fixed monthly payment
needed in order pay off a credit card balance within 12 months. By a
fixed monthly payment, we mean a single number which does not change
each month, but instead is a constant amount that will be paid each
month.

In this problem, we will not be dealing with a minimum monthly payment
rate. The following variables contain values as described below:

balance = the outstanding balance on the credit card
annualInterestRate = annual interest rate as a decimal

Assume that the interest is compounded monthly according to the balance
at the end of the month (after the payment for that month is made). The
monthly payment must be a multiple of $10 and is the same for all
months. Notice that it is possible for the balance to become negative
using this payment scheme, which is okay.
"""
# Declare initial balance and lowest monthly payment (lmp)
initialBalance = balance
lmp = 0
# Increasingly interate through possible lowest monthly payments
for fmp in range(10,initialBalance,10):
    balance = initialBalance
    # Iterate through balance changes every month
    for month in range (1,13):
        balance -= fmp
        balance *= (1 + annualInterestRate/12)
    # If balance at the end of a calendar year is 0 or less, we're done!
    if balance <= 0:
        lmp = fmp
        break
print("Lowest Payment: " + str(round(fmp, 2)))