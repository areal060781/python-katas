'''
Exercise 2: Write another program that prompts for a list of numbers
as above and at the end prints out both the maximum and minimum of
the numbers instead of the average.
'''
max = None
min = None
while True:
    value = input('Enter a number:  ')

    if value == 'done':
        break

    try:
        number = int(value)

        if (max is None or number > max):
            max = number
        if (min is None or number < min):
            min = number
    except (ValueError):
        print('Invalid input')
        continue


print(str(max) + ' ' + str(min))

