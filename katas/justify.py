'''Exercise 3.3. Python provides a built-in function called len that returns the length of a string, so
the value of len('allen') is 5.
Write a function named right_justify that takes a string named s as a parameter and prints the
string with enough leading spaces so that the last letter of the string is in column 70 of the display.
>>> right_justify('allen')'''


def right_justify(name):
    max_len = 71
    num_blank_spaces = max_len - len(name)

    return(' ' * num_blank_spaces + name)


name = 'allen'
name_justified = right_justify(name)
print(name_justified)
print(name_justified[70] == name[-1:])

