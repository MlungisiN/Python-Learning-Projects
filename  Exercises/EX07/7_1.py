# Write a program to read through a file and print the contents
# of the file (line by line) all in upper case.

file = open('mbox-short.txt')

for line in file:
    remove_line = line.rstrip( ) # remove new line chars
    print(remove_line.upper()) # convert to upper case
