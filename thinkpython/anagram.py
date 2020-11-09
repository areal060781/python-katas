def is_anagram(str1, str2):
    if len(str1) < 2 or len(str2) < 2:
        return False

    if str1 == str2:
        return False

    list1 = list(str1.lower())
    list2 = list(str2.lower())

    list1.sort()
    list2.sort()

    return list1 == list2

print(is_anagram('amor', 'roma'))
print(is_anagram('aida', 'aida'))
print(is_anagram('hola', 'lola'))