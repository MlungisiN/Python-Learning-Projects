

file_name = input('Enter the file name: ')
try:
    if file_name == 'na na boo boo':
        print('NA NA BOO BOO TO YOU - You have been punk\'d!')
        exit()
    file_open = open(file_name)

except FileNotFoundError:
    print('File cannot be opened:', file_name)
    exit()

count = 0
for line in file_open:
    if line.startswith('Subject:'):
        count += 1

print('There were', count, 'subject lines in', file_name)
