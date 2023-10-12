'''
Exercise 1: Write a function called chop that takes a list and modifies
it, removing the first and last elements, and returns None. Then write
a function called middle that takes a list and returns a new list that
contains all but the first and last elements.
'''


def chop(list):
    del list[0]
    del list[len(list)-1]


def middle(list):
    return list[1:-1]


input_list = list()

while (True):
    value = input('Enter a value: ')
    if value == 'done':
        break

    input_list.append(value)

print(input_list)

chop(input_list)

new_list = (middle(input_list))
print(input_list)
print(new_list)

print(input_list is new_list)


