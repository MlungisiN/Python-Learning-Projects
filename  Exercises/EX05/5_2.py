# Write another program that prompts for a list of numbers
# as above and at the end prints out both the maximum and minimum of
# the numbers instead of the average.

largest = None
smallest = None
while True:
    try:
        number = input('Enter a number: ')
        if number == 'done':
            break

        number = int(number)
        if largest is None or largest < number:
            largest = number
        elif smallest is None or smallest > number:
            smallest = number
    except:
        print('Invalid input')


print('Maximum is:', largest)
print('Minimum is:', smallest)
