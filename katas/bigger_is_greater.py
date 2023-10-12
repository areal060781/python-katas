'''
https://www.hackerrank.com/challenges/bigger-is-greater/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
lexicographical permutation algorithm
'''


def bigger_is_greater(w):
    wmax, wmin = max(w), min(w)
    lword = len(w)

    # same letter
    if wmax == wmin:
        return 'no answer'

    # descendant order
    # if wmax == w[0] and wmin == w[-1]:
    #     return 'no answer'

    if w[-1] > w[-2]:
        return w[:-2] + w[-1] + w[-2]
    else:
        initial_index = lword * -1
        swap_index = None
        next_greater_index = -1
        b_flag = False

        while next_greater_index > initial_index:
            for i in range(next_greater_index - 1, initial_index - 1, -1):
                if w[next_greater_index] > w[i]:
                    swap_index = i
                    b_flag = True
                    break

            if b_flag:
                break

            if swap_index is None:
                next_greater_index -= 1

        print('next_greater_index: ', next_greater_index, ' swap_index: ', swap_index)
        if swap_index is None:
            return 'no answer'
        elif swap_index == initial_index:
            return w[next_greater_index:] + w[swap_index:next_greater_index]
        else:
            return w[initial_index:swap_index] + w[next_greater_index:] + w[swap_index:next_greater_index]


def bigger_is_greater2(w):
    arr = list(w)
    # Find non-increasing suffix
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1

    if i <= 0:
        return "no answer"

    # Find successor to pivot
    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1

    print('i:',  i, 'j:',  j)

    arr[i - 1], arr[j] = arr[j], arr[i - 1]

    # Reverse suffix
    arr[i:] = arr[len(arr) - 1: i - 1: -1]

    return "".join(arr)