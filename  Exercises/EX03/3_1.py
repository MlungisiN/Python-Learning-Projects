# Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

hours = input('Enter Hours:', )
rate = input('Enter Rate:', )
hours = int(hours)
rate = int(rate)
pay = hours * rate

if hours > 40:
    print('Overtime')
    regular = hours * rate
    overtime = (hours - 40) * (rate * 0.5)
    print(regular, overtime)
    pay = regular + overtime
else:
    print('Regular')
print('Your Pay is:', pay)
