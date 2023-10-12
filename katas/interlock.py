"""Exercise 10.13. Two words “interlock” if taking alternating letters from each forms a new
word. For example, “shoe” and “cold” interlock to form “schooled.” Solution: http: //
think_python. com/ code/ interlock. py . Credit: This exercise is inspired by an example at
http: // puzzlers. org .

"""

from binary_or_bisection_search import *


def interlock(word_list, word):
    """Checks whether a word can be split into two interlocked words.

    word_list: list of strings
    word: string
    """
    evens = word[::2]
    odds = word[1::2]
    return in_bisect(word_list, evens) and in_bisect(word_list, odds) 
        

def interlock_general(word_list, word, n=3):
    """Checks whether a word can be split into n interlocked words.

    word_list: list of strings
    word: string
    n: number of interleaved words
    """
    for i in range(n):
        inter = word[i::n]
        if not in_bisect(word_list, inter):
            return False
    return True
        

if __name__ == '__main__':
    word_list = make_word_list()
    
    for word in word_list:
        if interlock(word_list, word):
            print(word, word[::2], word[1::2])


#    for word in word_list:
#        if interlock_general(word_list, word, 3):
#            print word, word[0::3], word[1::3], word[2::3]


