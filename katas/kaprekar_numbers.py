'''
A modified Kaprekar number is a positive whole number with a special property. If you square it, then split the number
into two integers and sum those integers, you have the same value you started with.
'''


def kaprekar_numbers(p, q):
    o = list()
    for n in range(p, q + 1):
        l1 = len(str(n))
        sqr = n ** 2
        l2 = len(str(sqr))

        l = int(str(sqr)[0:l1])

        if l2 == l1:
            r = 0
        elif l2 == l1 * 2:
            r = int(str(sqr)[l1:])
        elif l2 == (l1 * 2) - 1:
            l = int(str(sqr)[0:l1 - 1])
            r = int(str(sqr)[l2 - l1:])

        if l + r == n:
            o.append(n)

    if o:
        o.sort()
        return ' '.join(map(str, o))
    else:
        return 'INVALID RANGE'
