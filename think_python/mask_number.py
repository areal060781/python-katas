def mask_number(in_string):
    mask_character = '#'
    unmask_long = 4

    if len(in_string) < unmask_long:
        print('We can not mask the given number')

    long_to_mask = len(in_string[:-4])
    unmask_str = in_string[-4:]

    return long_to_mask * mask_character + unmask_str


in_string = input('Type a string to mask: ')
print(mask_number(in_string))

