'''Exercise 3.5. This exercise can be done using only the statements and other features we have learned
so far.
1. Write a function that draws a grid like the following:
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
Hint: to print more than one value on a line, you can print a comma-separated sequence:
print '+', '-'
If the sequence ends with a comma, Python leaves the line unfinished, so the value printed
next appears on the same line.
print '+',
print '-'
The output of these statements is '+ -' .
A print statement all by itself ends the current line and goes to the next line.
2. Write a function that draws a similar grid with four rows and four columns.
Solution: http: // thinkpython. com/ code/ grid. py . Credit: This exercise is based on an
exercise in Oualline, Practical C Programming, Third Edition, O’Reilly Media, 1997.'''


def do_twice(f):
    f()
    f()


def do_four(f):
    do_twice(f)
    do_twice(f)


def print_beam():
    print('+ - - - -', end='')


def print_post():
    print('|        ', end='')


def print_beams():
    do_twice(print_beam)
    print('+')


def print_posts():
    do_twice(print_post)
    print('|')


def print_row():
    print_beams()
    do_four(print_posts)


def print_grid():
    do_twice(print_row)
    print_beams()


print_grid()