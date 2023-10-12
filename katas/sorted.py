def is_sorted(l):
    previous = l[0]
    for c in l:
        if c < previous:
            return False
        previous = c
    return True



print(is_sorted([1,2,2]))
print(is_sorted(['b','a']))
print(is_sorted(['a','b','c']))