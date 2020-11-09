'''
Given the time in numerals we may convert it into words, as shown below:

At , use o' clock. For , use past, and for  use to. Note the space between the apostrophe and clock in o' clock. Write a
program which prints the time in words for the input given in the format described.

Function Description

Complete the timeInWords function in the editor below. It should return a time string as described.

timeInWords has the following parameter(s):

h: an integer representing hour of the day
m: an integer representing minutes after the hour
'''


def number_in_words(n):
    words1 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
              'thirteen', 'fourteen', 'quarter', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    words2 = ['twenty', 'half']

    if 0 <= n <= 19:
        return words1[n]
    elif 20 <= n <= 99:
        tens, remain = divmod(n, 10)
        return words2[tens - 2] + ' ' + words1[remain] if remain else words2[tens - 2]


def time_in_words(h, m):
    w = list()
    if m == 0:
        return number_in_words(h) + " o' clock"
    elif m > 30:
        m = 60 - m
        h += 1
        w.append('to')
    else:
        w.append('past')

    if m == 1:
        w.append('minute')
    elif m != 15 and m != 30:
        w.append('minutes')

    w.reverse()

    t = list()
    t.append(number_in_words(m))
    t.append(' '.join(w))
    t.append(number_in_words(h))

    return ' '.join(t)
