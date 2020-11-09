import math


def min_sum(num, k):
    l = len(num)

    if k > l:
        t = k // l
        for i in range(0, t):
            num = [math.ceil(n / 2) for n in num]
        k -= t * l

    for i in range(0, k):
        max_i = num.index(max(num))
        num[max_i] = math.ceil(num[max_i] / 2)

    return sum(num)
