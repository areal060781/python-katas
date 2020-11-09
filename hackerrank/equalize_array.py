def equalizeArray(arr):
    d = dict()
    for c in arr:
        d[c] = d.get(c, 0) + 1

    max_val = max(d, key=d.get)
    print(d, max_val)
    return (len(arr) - d[max_val])

equalizeArray([1,2, 3, 1, 2, 3, 3, 3])