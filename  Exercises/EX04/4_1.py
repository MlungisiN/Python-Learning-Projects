# Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).

def computepay(hours, rate):
    if hours > 40:
        regular = hours * rate
        overtime = (hours - 40) * (rate * 0.5)
        pay = regular + overtime
    else:
        pay = hours * rate
    return(pay)

hours = input('Enter Hours:', )
rate = input('Enter Rate:', )
hours = int(hours)
rate = int(rate)

amount = computepay(hours, rate)
print('Your Pay is:', amount)
