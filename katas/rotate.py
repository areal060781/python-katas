"""ROT13 is a weak form of encryption that involves “rotating” each letter in a word
by 13 places. To rotate a letter means to shift it through the alphabet, wrapping around to the
beginning if necessary, so ’A’ shifted by 3 is ’D’ and ’Z’ shifted by 1 is ’A’.
Write a function called rotate_word that takes a string and an integer as parameters, and that
returns a new string that contains the letters from the original string “rotated” by the given amount.
For example, “cheer” rotated by 7 is “jolly” and “melon” rotated by -10 is “cubed”.
You might want to use the built-in functions ord , which converts a character to a numeric code,
and chr , which converts numeric codes to characters.

"""

import string


def rotate_letter(letter, n):
    """Rotates a letter by n places.  Does not change other chars.

    letter: single-letter string
    n: int

    Returns: single-letter string
    """
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter

    c = ord(letter) - start
    i = (c + n) % 26 + start
    return chr(i)


def rotate_word(word, n):
    """Rotates a word by n places.

    word: string
    n: integer

    Returns: string
    """
    res = ''
    for letter in word:
        res += rotate_letter(letter, n)
    return res


if __name__ == '__main__':
    print(rotate_word('ZOLOF', 1))
    print(rotate_word('APMPG', 25))
    print(rotate_word('aida', 13))
    print(rotate_word('nvqn', 13))
    # print(rotate_word('cheer', 7))
    # print(rotate_word('melon', -10))
    # print(rotate_word('sleep', 9))
