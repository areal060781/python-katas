'''
https://www.hackerrank.com/challenges/bigger-is-greater/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
'''


def bigger_is_greater(w):
    wmax, wmin = max(w), min(w)
    lword = len(w)

    # same letter
    if wmax == wmin:
        return 'no answer'

    # descendant order
    if wmax == w[0] and wmin == w[-1]:
        return 'no answer'

    if w[-1] > w[-2]:
        return w[:-2] + w[-1] + w[-2]
    else:
        swap_index = None
        next_greater_index = -2 if w[-1] == wmin else -1
        initial_index = lword * -1

        for i in range(next_greater_index - 1, initial_index - 1, -1):
            if w[next_greater_index] > w[i]:
                swap_index = i
                break

        if swap_index == initial_index:
            return w[next_greater_index:] + w[swap_index:next_greater_index]
        else:
            return w[initial_index:swap_index] + w[next_greater_index:] + w[swap_index:next_greater_index]

    # if w[-1] == wmin:
    #     print("1 The last letter is the minimum one")
    #     swap_index = None
    #     next_greater_index = -2
    #
    #     for i in range(next_greater_index - 1, -1 * (lword + 1), -1):
    #         if w[next_greater_index] > w[i]:
    #             swap_index = i
    #             break
    #
    #     if swap_index == lword * -1:
    #         return w[next_greater_index:] + w[swap_index:next_greater_index]
    #     else:
    #         return w[lword * -1:swap_index] + w[next_greater_index:] + w[swap_index:next_greater_index]
    # elif w[-1] > w[-2]:
    #     print("3 The last letter is greater than its next one")
    #     return w[:-2] + w[-1] + w[-2]
    # else:
    #     print("2 The last letter is not greater than its next one but neither is the minimum one")
    #     swap_index = None
    #     next_greater_index = -1
    #     for i in range(-2, -1 * (lword + 1), -1):
    #         if w[-1] > w[i]:
    #             swap_index = i
    #             break
    #
    #     if swap_index == lword * -1:
    #         return w[next_greater_index:] + w[swap_index:next_greater_index]
    #     else:
    #         return w[lword * -1:swap_index] + w[next_greater_index:] + w[swap_index:next_greater_index]
