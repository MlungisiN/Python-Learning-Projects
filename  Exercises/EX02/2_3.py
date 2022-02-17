# Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.

celsius = input('What is the Temperature:', )
celsius = int(celsius)
fahrenheit = (celsius * 9/5) + 32

print(fahrenheit)
