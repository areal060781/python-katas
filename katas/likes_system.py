def likes_mine(names):
    num_items = len(names)

    if num_items == 0:
        return 'no one likes this'
    if num_items == 1:
        return f"{names[0]} likes this"
    if num_items == 2:
        return f"{' and '.join(names)} like this"
    if num_items == 3:
        return f"{', '.join(names[:2])} and {names[-1]} like this"
    return f"{', '.join(names[:2])} and {len(names[2:])} others like this"


def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n - 2)
