# Rewrite your pay program using try and except so that your
program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:

hours = input('Enter Hours:', )
rate = input('Enter Rate:', )
try:
    hours = int(hours)
    rate = int(rate)
except:
    print('Error, please enter numeric input')
    quit()

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
