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
monthly payment is the same for all months and can be ANY dollar amount.
The balance should NOT to become negative using this payment scheme.
"""
# Declare initial balance and high/low guesses, and initial fmp guess
initialBalance = balance
low = initialBalance/12
high = initialBalance
fmp = (low + high)/2
# Bisection search through fmp guesses until balance is near zero
while balance >= 0.01 or balance <= -0.01:
    balance = initialBalance
    for month in range(1,13):
        balance -= fmp
        balance *= (1 + annualInterestRate/12)
    if balance > 0:
        low = fmp
    else:
        high = fmp
    fmp = (low + high)/2
print("Lowest Payment: " + str(round(fmp,2)))
