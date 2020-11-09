def cut_the_sticks(arr):
    l = len(arr)
    r = [l]

    if sum(arr) == l:
        return r

    while l > 1:
        m = min(arr)
        arr = [e - m for e in arr if (e - m) > 0]
        l = len(arr)
        if l > 0:
            r.append(l)
    return r

