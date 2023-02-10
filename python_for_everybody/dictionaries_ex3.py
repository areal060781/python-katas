# Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary to count how many
# messages have come from each email address, and print the dictionary.
#
# Enter file name: mbox-short.txt
# {'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
# 'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
# 'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
# 'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
# 'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
# 'ray@media.berkeley.edu': 1}

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
        mail = words[1]
        output_dict[mail] = output_dict.get(mail, 0) + 1

print(output_dict)
