# Write a program to look for lines of the form:
# New Revision: 39772
#
# Extract the number from each of the lines using a regular expression and the findall() method. Compute the average of
# the numbers and print out the average.
#
# Enter file:mbox.txt
# 38444.0323119
#
# Enter file:mbox-short.txt
# 39756.9259259

import re
from config import basedir

file = input('Enter a file name: ')
filename = basedir.joinpath('..', 'static', file)

try:
    handle = open(filename.absolute())
except:
    print('File cannot be opened: ', file)
    exit()

sum = 0
count = 0
for line in handle:
    line = line.rstrip()
    revisions = re.findall('^New Revision: ([0-9]+)', line)
    if len(revisions) > 0:
        sum += int(revisions[0])
        count += 1

print(sum/count)
