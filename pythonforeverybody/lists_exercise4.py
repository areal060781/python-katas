'''
Exercise 4: Download a copy of the file www.py4e.com/code3/romeo.txt.
Write a program to open the file romeo.txt and read it line by line. For
each line, split the line into a list of words using the split function.
For each word, check to see if the word is already in a list. If the word
is not in the list, add it to the list. When the program completes, sort
and print the resulting words in alphabetical order.
'''


handle = open('romeo.txt')
word_list = list()

for line in handle:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if not(word in word_list):
            word_list.append(word)

word_list.sort()
print(word_list)