# Exercise 2: Write a program that categorizes each mail message by which day of the week the commit was done.
# To do this look for lines that start with “From”, then look for the third word and keep a running count of each of
# the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).
#
# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan
#
# Sample Execution:
# python dow.py
# Enter a file name: mbox-short.txt
# {'Fri': 20, 'Thu': 6, 'Sat': 1}


from config import basedir

file = input('Enter a file name: ')
filename = basedir.joinpath('..', 'static', file)

try:
    handle = open(filename.absolute())
except:
    print('File cannot be opened: ', file)
    exit()

output_dict = dict()
for line in handle:
    line = line.rstrip()
    if line.startswith('From '):
        words = line.split()
        day = words[2]
        output_dict[day] = output_dict.get(day, 0) + 1
        # if day not in output_dict:
        #     output_dict[day] = 1
        # else:
        #     output_dict[day] += 1

print(output_dict)
