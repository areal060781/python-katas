'''
Exercise 4: Add code to the above program to figure out who has the most messages in the file. After all the data has
been read and the dictionary has been created, look through the dictionary using a maximum loop (see Chapter 5: Maximum
and minimum loops) to find who has the most messages and print how many messages the person has.

Enter a file name: mbox-short.txt
cwen@iupui.edu 5
Enter a file name: mbox.txt
zqian@umich.edu 195
'''

file = input('Enter a file name: ')

try:
    handle = open(file)
except:
    print('File cannot be opened: ', file)
    exit()

output_dict = dict()
for line in handle:
    line = line.rstrip()
    if line.startswith('From '):
        words = line.split()
        mail = words[1]
        output_dict[mail] = output_dict.get(mail, 0) + 1

largest = None
key = None
for mail in output_dict:
    if largest is None or output_dict[mail] > largest:
        largest = output_dict[mail]
        key = mail

print('%s %s' % (key, largest))
