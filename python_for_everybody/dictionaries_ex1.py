'''Write a program that reads the words in words.txt and stores them as
keys in a dictionary. It doesn’t matter what the values are. Then you
can use the in operator as a fast way to check whether a string is in the
dictionary.'''
from config import basedir

filename = basedir.joinpath('..', 'static', 'words.txt')

handle = open(filename.absolute())

output_dict =  dict()
for line in handle:
    line = line.rstrip()
    words = line.split()
    for word in words:
        output_dict[word] = 'aida'

while (True):
    word = input('Enter a word: ')
    if word == 'done':
        break

    if (word in output_dict):
        print('The word %s exists' % word)
    else:
        print('The word %s NO exists' % word)