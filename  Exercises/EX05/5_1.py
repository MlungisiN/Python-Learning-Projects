# Write a program which repeatedly reads numbers until the
# user enters “done”. Once “done” is entered, print out the total, count,
# and average of the numbers. If the user enters anything other than a
# number, detect their mistake using try and except and print an error
# message and skip to the next number.

number = 0
total = 0.0
while True:
    value = input('Enter a number: ')
    if value == 'done':
        break
    try:
        ivalue = int(value)
    except:
        print('Invalid input')
    number = number + 1
    total = total + ivalue

print(total, number, total/number)
