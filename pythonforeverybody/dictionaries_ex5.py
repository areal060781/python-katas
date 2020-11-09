'''
Exercise 5: This program records the domain name (instead of the address) where the message was sent from instead of
who the mail came from (i.e., the whole email address). At the end of the program, print out the contents of your
dictionary.

python schoolcount.py
Enter a file name: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7, 'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}
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
        mail = words[1].split('@')
        domain = mail[1]
        output_dict[domain] = output_dict.get(domain, 0) + 1

print(output_dict)