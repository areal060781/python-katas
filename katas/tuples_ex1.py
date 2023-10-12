
# Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line. Count
# the number of messages from each person using a dictionary. After all the data has been read, print the person with
# the most commits by creating a list of (count, email) tuples from the dictionary. Then sort the list in reverse order
# and print out the person who has the most commits.
#
# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
#
# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5
#
# Enter a file name: mbox.txt
# zqian@umich.edu 195

# Read and open the file
from config import basedir

file = input('Enter a file name: ')
filename = basedir.joinpath('..', 'static', file)

try:
    handle = open(filename.absolute())
except:
    print('File cannot be opened:', file)
    exit()

# Traverse the file and get the hystogram by email (dictionary)
counts = dict()
for line in handle:
    line = line.rstrip()
    if line.startswith('From '):
        words = line.split()
        mail = words[1]
        counts[mail] = counts.get(mail, 0) + 1

# Print the person with the mos commits (list of tuples) by sorting the list in reverse order
lst = list()
for key, val in list(counts.items()):
    lst.append((val,key))

lst.sort(reverse=True)

for key, val in lst[:1]:
    print(key, val)