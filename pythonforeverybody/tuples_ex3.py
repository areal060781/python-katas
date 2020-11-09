'''
Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency. Your program should
convert all the input to lower case and only count the letters a-z. Your program should not count spaces, digits,
punctuation, or anything other than the letters a-z. Find text samples from several different languages and see how
letter frequency varies between languages. Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.
'''
import string
import unidecode

# Read and open the file
file = input('Enter a file name: ')

try:
    handle = open(file)
except:
    print('File cannot be opened:', file)
    exit()


# Traverse the file and get the frequence by letter (dictionary)
counts = dict()
for line in handle:
    line = line.rstrip()
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.translate(str.maketrans('', '', string.digits))
    line = line.translate(str.maketrans('', '', string.whitespace))
    line = line.lower()
    line = unidecode.unidecode(line)
    letters = list(line)
    for letter in letters:
        counts[letter] = counts.get(letter, 0) + 1

# prints the letters in decreasing order of frequency
lst = list()
for key, val in list(counts.items()):
    lst.append((val,key))

lst.sort(reverse=True)

for key, val in lst:
    print(key, val)