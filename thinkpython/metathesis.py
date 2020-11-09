"""Exercise 12.5. Two words form a “metathesis pair” if you can transform one into the other by
swapping two letters; for example, “converse” and “conserve.” Write a program that finds all of
the metathesis pairs in the dictionary. Hint: don’t test all pairs of words, and don’t test all possible
swaps. Solution: http: // thinkpython. com/ code/ metathesis. py .

"""

from anagram_sets import *

def metathesis_pairs(d):
    """Print all pairs of words that differ by swapping two letters.

    d: map from word to list of anagrams
    """
    for anagrams in iter(d.values()):
        for word1 in anagrams:
            for word2 in anagrams:
                if word1 < word2 and word_distance(word1, word2) == 2:
                    print(word1, word2)


def word_distance(word1, word2):
    """Computes the number of differences between two words.

    word1, word2: strings

    Returns: integer
    """
    assert len(word1) == len(word2)

    count = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            count += 1

    return count


if __name__ == '__main__':
    d = all_anagrams('words.txt')
    metathesis_pairs(d)
