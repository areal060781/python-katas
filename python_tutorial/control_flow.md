# 4. More Control flows tools
https://docs.python.org/3/tutorial/controlflow.html
https://docs.python.org/3/reference/index.html

## Slicing
```python
word = "Python"
print(word[0])  # Character in position 0
print(word[-1])  # last character, since -0 is the same as 0
print(word[0:2])  # "Py" characters from position 0 (included) to 2 (excluded)

print(word[:2])  # "Py" ommited first index defauts to zero
print(word[4:])  # "on" ommited second index defualts to the size of the string being sliced
```
## For statement
The for statement in Python differs a bit from other languages. Rather than always iterating
over an arithmetic progression of numbers, or giving the user the ability to define both the
iteration step and halting condition,
Python’s for statement iterates over the items of any sequence (a list or a string),
in the order that they appear in the sequence
```python
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
```
Code that modifies a collection while iterating over that same collection can be tricky to get right.
Instead, it is usually more straight-forward to loop over a copy of the collection or to create a
new collection:
Create a sample collection
```python
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
```
## Range function
```python
for i in range(5):
    print(i)
```
## break and continue Statements, and else Clauses on Loops

## pass statement

## Match statement (switch)
```python
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
```
## Keyword Arguments kwarg=value
```python
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
```
accepts one required argument (voltage) and three optional arguments (state, action, and type).
This function can be called in any of the following ways
```python
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
```
When a final formal parameter of the form **name is present, it receives a dictionary
(see Mapping Types — dict) containing all keyword arguments except for those corresponding to a
formal parameter. This may be combined with a formal parameter of the form *name (described in the
next subsection) which receives a tuple containing the positional arguments beyond the formal
parameter list. (*name must occur before **name.) For example, if we define a function like this:
```python
def cheeseshop(kind, *tuple, **dictionary):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in tuple:
        print(arg)
    print("-" * 40)
    for kw in dictionary:
        print(kw, ":", dictionary[kw])
```
It could be called like this:
```python
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
```
## Special parameters
# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
#       -----------    ----------     ----------
#         |             |                  |
#         |        Positional or keyword   |
#         |                                - Keyword only
#          -- Positional only
# where / and * are optional. If used, these symbols indicate the kind of parameter by how the
# arguments may be passed to the function: positional-only, positional-or-keyword, and keyword-only.
# Keyword parameters are also referred to as named parameters.

## Lambda expressions
```python
def make_incrementor(n):
    return lambda x: x+n

# f = make_incrementor(42)
# f(0)
# 42
# f(1)
# 43
```
## Documentation Strings
The first line should always be a short, concise summary of the object’s purpose. For brevity,
it should not explicitly state the object’s name or type, since these are available by other means
(except if the name happens to be a verb describing a function’s operation). This line should begin
with a capital letter and end with a period.
If there are more lines in the documentation string, the second line should be blank, visually
separating the summary from the rest of the description. The following lines should be one or
more paragraphs describing the object’s calling conventions, its side effects, etc.
```python
def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass
```
## Coding style PEP8
* Use 4-space indentation, and no tabs.
* 4 spaces are a good compromise between small indentation (allows greater nesting depth) and large indentation (easier to read). Tabs introduce confusion, and are best left out.
* Wrap lines so that they don’t exceed 79 characters.
* This helps users with small displays and makes it possible to have several code files side-by-side on larger displays.
* Use blank lines to separate functions and classes, and larger blocks of code inside functions.
* When possible, put comments on a line of their own.
* Use docstrings.
* Use spaces around operators and after commas, but not directly inside bracketing constructs: a = f(1, 2) + g(3, 4).
* Name your classes and functions consistently; the convention is to use UpperCamelCase for classes and lowercase_with_underscores for functions and methods. Always use self as the name for the first method argument (see A First Look at Classes for more on classes and methods).
* Don’t use fancy encodings if your code is meant to be used in international environments. Python’s default, UTF-8, or even plain ASCII work best in any case.
* Likewise, don’t use non-ASCII characters in identifiers if there is only the slightest chance people speaking a different language will read or maintain the code