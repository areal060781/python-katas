def has_no_e(word):
    # for letter in word:
    #     if letter == 'e':
    #         return False
    # return True

    return word.find('e') != -1


def avoids(word, forbidden):
    # for letter in word:
    #     if letter in forbidden:
    #         return False
    # return True

    for i in range(0, len(forbidden)):
        if word.find(forbidden[i]) != -1:
            return False
    return True


def uses_only(word, available):
    for letter in word:
        if letter not in available:
            return False
    return True

def uses_all(word, required):
    for letter in required:
        if letter not in word:
            return False
    return True

    # for i in range(0, len(available)):
    #     if word.find(available[i]) == -1:
    #         return False
    # return True

def is_abecedarian(word):
    previous = word[0]
    for c in word:
        if c < previous:
            return False
        previous = c
    return True

    # i = 0
    # while i < len(word) - 1:
    #     if word[i + 1] < word[i]:
    #         return False
    # i = i + 1
    # return True

    # if len(word) <= 1:
    #     return True
    # if word[0] > word[1]:
    #     return False
    # return is_abecedarian(word[1:])

# forbidden = input("Type the forbidden letters: ")
# only = input("Type the only letters: ")
file = open('words.txt')

total_words = 113809
words_without_e = 0

for line in file:
    line = line.strip()
    # if len(line) > 20:
    #     print(line)

    # if has_no_e(line) == True:
    #     words_without_e += 1

    # if avoids(line, forbidden) == True:
    #     print(line)

    # if uses_only(line, only) == True:
    #     print(line)

    if is_abecedarian(line) == True:
        print(line)

# e_percentage = words_without_e * 100 / total_words
# print("%d Total of words without e." % words_without_e)
# print("%f Percentage of words without e." % e_percentage)