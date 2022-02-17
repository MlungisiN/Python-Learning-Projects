# Write a program to prompt the user for hours and rate per hour to compute gross pay.

hours = input('Enter Hours:', )
rate = input('Enter Rate:', )
hours = int(hours)
rate = int(rate)
pay = hours * rate
print('Your Pay is:', pay)
