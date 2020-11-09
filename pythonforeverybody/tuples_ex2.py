'''
Exercise 2: This program counts the distribution of the hour of the day for each of the messages. You can pull the hour
from the “From” line by finding the time string and then splitting that string into parts using the colon character.
Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.

python timeofday.py
Enter a file name: mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
'''

# Read and open the file
file = input('Enter a file name: ')

try:
    handle = open(file)
except:
    print('File cannot be opened:', file)
    exit()

# Traverse the file and get the hystogram by email (dictionary)
counts = dict()
for line in handle:
    line = line.rstrip()
    if line.startswith('From '):
        words = line.split()
        time = words[5]
        hour, minute, second = time.split(':')
        counts[hour] = counts.get(hour, 0) + 1

# Print the hour with the most commits (list of tuples) by sorting the list in order
lst = list()
for key, val in list(counts.items()):
    lst.append((key,val))

lst.sort()

for key, val in lst:
    print(key, val)