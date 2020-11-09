"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

def first(word):
    """Returns the first character of a string."""
    return word[0]


def last(word):
    """Returns the last character of a string."""
    return word[-1]


def middle(word):
    """Returns all but the first and last characters of a string."""
    return word[1:-1]


def is_palindrome(word):
    """Returns True if word is a palindrome."""
    print(word)
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))


print(is_palindrome('allen'))
print(is_palindrome('bob'))
print(is_palindrome('otto'))
print(is_palindrome('redivider'))


def is_palindrome_improved(word):
    return word == word[::-1]


print()
print(is_palindrome_improved('allen'))
print(is_palindrome_improved('bob'))
print(is_palindrome_improved('otto'))
print(is_palindrome_improved('redivider'))
